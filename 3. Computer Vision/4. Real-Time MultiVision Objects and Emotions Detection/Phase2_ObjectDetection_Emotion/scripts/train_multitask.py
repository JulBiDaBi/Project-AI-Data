# Phase2/train/train_multitask.py
"""
Entraînement multitâche simple compatible avec :
 - Phase2.models.multitask_model.MultitaskYOLO
 - Phase2.datasets.multitask_dataloader.get_multitask_loader

Fonctionnalités :
 - Entraîne la tête émotion (CrossEntropy) sur les images AffectNet (batch emo_imgs)
 - Tente d'entraîner la tête détection via la loss interne Ultralytics (si disponible) sur det_imgs.
 - Fallback : si la loss détection n'est pas disponible, seule la tête émotion est entraînée.
 - Checkpointing, logs, sauvegarde du meilleur modèle par epoch.

Usage (exemple) :
 python train_multitask.py \
     --obj_model /kaggle/working/pretrained/yolov8m.pt \
     --emo_model /kaggle/working/models/yolov8m_emotions_affectnet.pt \
     --detection_root /kaggle/working/coco \
     --emotion_root /kaggle/working/data/YOLO_format \
     --epochs 20 --batch_size 8
"""

import os
import argparse
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.optim as optim

from ultralytics import YOLO

# Importer ton modèle et dataloader (chemins relatifs à la racine du repo)
from Phase2.models.multitask_model import MultitaskYOLO
from Phase2.datasets.multitask_dataloader import get_multitask_loader


def try_get_ultralytics_detect_loss(yolo_path):
    """
    Tente d'instancier un objet YOLO (Ultralytics) et de localiser une fonction de loss.
    Retourne (yolo_obj, detect_module, has_loss_callable)
    """
    try:
        yolo_wrapper = YOLO(yolo_path)
    except Exception as e:
        print(f"[WARN] Impossible d'instancier YOLO({yolo_path}): {e}")
        return None, None, False

    # Plusieurs versions d'Ultralytics ont des objets internes différents.
    # On tente plusieurs accès.
    detect_module = None
    if hasattr(yolo_wrapper, "model"):
        # wrapper.model peut être un nn.Module (avec .model list) ou un Model object
        inner = yolo_wrapper.model
        # try inner.model if present
        if hasattr(inner, "model"):
            # inner.model is often a nn.ModuleList
            mlist = inner.model
            try:
                detect_module = mlist[-1]
            except Exception:
                detect_module = None
        else:
            # inner itself might be modulelist-like
            try:
                detect_module = list(inner.children())[-1]
            except Exception:
                detect_module = None

    # Check for loss method
    has_loss = False
    if detect_module is not None:
        # common names: loss, compute_loss, detect_loss
        if hasattr(detect_module, "loss") or hasattr(detect_module, "compute_loss"):
            has_loss = True
    return yolo_wrapper, detect_module, has_loss


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--obj_model", type=str, required=True,
                   help="Path to base detection YOLO model (e.g. yolov8m.pt)")
    p.add_argument("--emo_model", type=str, required=True,
                   help="Path to pretrained emotion YOLO model (phase1)")
    p.add_argument("--detection_root", type=str, required=True,
                   help="Root folder for detection dataset (must contain images/ and labels/ subfolders)")
    p.add_argument("--emotion_root", type=str, required=True,
                   help="Root folder for emotion dataset (YOLO format: images/, labels/)")
    p.add_argument("--epochs", type=int, default=20)
    p.add_argument("--batch_size", type=int, default=8)
    p.add_argument("--img_size", type=int, default=640)
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--weight_decay", type=float, default=1e-4)
    p.add_argument("--save_dir", type=str, default="/kaggle/working/checkpoints")
    p.add_argument("--device", type=str, default="cuda:0" if torch.cuda.is_available() else "cpu")
    p.add_argument("--freeze_backbone", action="store_true", help="Freeze shared backbone weights")
    p.add_argument("--w_obj", type=float, default=1.0, help="Weight for object detection loss")
    p.add_argument("--w_emo", type=float, default=1.0, help="Weight for emotion classification loss")
    return p.parse_args()


def collate_det_labels_to_targets(det_labels_batch):
    """
    det_labels_batch : list of [N_i x 5] tensors (class, x,y,w,h), normalized
    We need to convert to the format expected by any detect loss if available.
    Many implementations expect targets as a tensor [num_targets, 6] = (img_idx, cls, x, y, w, h)
    If not used, this function still returns a plausible tensor.
    """
    targets = []
    for img_idx, lbls in enumerate(det_labels_batch):
        if isinstance(lbls, torch.Tensor) and lbls.numel() > 0:
            # lbls shape Nx5
            for row in lbls.detach().cpu().numpy():
                cls = int(row[0])
                x, y, w, h = float(row[1]), float(row[2]), float(row[3]), float(row[4])
                targets.append([img_idx, cls, x, y, w, h])
    if len(targets) == 0:
        return torch.zeros((0, 6), dtype=torch.float32)
    return torch.tensor(targets, dtype=torch.float32)


def main():
    args = parse_args()
    os.makedirs(args.save_dir, exist_ok=True)

    device = args.device

    print(f"[INFO] Device: {device}")
    print("[INFO] Building dataloader...")
    # get_multitask_loader returns DataLoader with batches: dict keys det_imgs, det_labels, emo_imgs, emo_labels
    loader = get_multitask_loader(
        detection_root=args.detection_root,
        emotion_root=args.emotion_root,
        batch_size=args.batch_size,
        img_size=args.img_size,
        shuffle=True,
        num_workers=4,
    )

    print("[INFO] Instantiating Multitask model...")
    model = MultitaskYOLO(detection_model_name=args.obj_model,
                          emotion_model_path=args.emo_model,
                          num_emotions=8,
                          freeze_backbone=args.freeze_backbone)
    model.to(device)

    # Setup optimizer: only params with requires_grad = True
    params_to_train = [p for p in model.parameters() if p.requires_grad]
    optimizer = optim.AdamW(params_to_train, lr=args.lr, weight_decay=args.weight_decay)

    # Loss for emotions (classification)
    criterion_emo = nn.CrossEntropyLoss()

    # Try to obtain Ultralytics detect loss wrapper (best-effort)
    print("[INFO] Attempting to access Ultralytics detect loss (best-effort)...")
    yolo_wrapper, detect_module, has_detect_loss = try_get_ultralytics_detect_loss(args.obj_model)
    if has_detect_loss:
        print("[INFO] Found detect module with loss callable. Will attempt to compute detection loss via Ultralytics internals.")
    else:
        print("[WARN] Could not find a detect loss callable in Ultralytics model. Detection loss will be skipped (only emotion head will be trained).")

    best_emo_acc = 0.0

    for epoch in range(1, args.epochs + 1):
        model.train()
        epoch_loss = 0.0
        epoch_emo_loss = 0.0
        epoch_obj_loss = 0.0
        num_batches = 0

        pbar = tqdm(loader, desc=f"Epoch {epoch}/{args.epochs}")
        for batch in pbar:
            # batch: dict with det_imgs, det_labels, emo_imgs, emo_labels
            det_imgs = batch["det_imgs"].to(device)           # [B,3,H,W]
            emo_imgs = batch["emo_imgs"].to(device)           # [B,3,H,W]
            det_labels = batch["det_labels"]                  # list of tensors per image
            emo_labels = batch["emo_labels"].to(device).long()# [B] long (class idx) (-1 if missing)

            optimizer.zero_grad()

            # -------------------------
            # Forward detection images -> detection outputs
            # -------------------------
            with torch.set_grad_enabled(True):
                det_out, _ = model(det_imgs)   # detection_out, emotions_logits
                # det_out: format depends on detection head (raw preds)
                loss_obj = torch.tensor(0.0, device=device)

                if has_detect_loss and detect_module is not None:
                    # Build targets in common expected format: [img_idx, cls, x, y, w, h]
                    targets = collate_det_labels_to_targets(det_labels).to(device)
                    try:
                        # Try a few possible call signatures for loss:
                        # 1) detect_module.loss(pred, targets, imgs=..., model=...)
                        # 2) yolo_wrapper.model.loss(preds, targets)
                        # 3) yolo_wrapper.loss(preds, targets)
                        if hasattr(detect_module, "loss"):
                            # Some impls expect preds, targets, and possibly other args.
                            loss_obj = detect_module.loss(det_out, targets)
                        elif hasattr(yolo_wrapper.model, "loss"):
                            loss_obj = yolo_wrapper.model.loss(det_out, targets)
                        elif hasattr(yolo_wrapper, "loss"):
                            loss_obj = yolo_wrapper.loss(det_out, targets)
                        else:
                            # final fallback: set zero
                            loss_obj = torch.tensor(0.0, device=device)
                    except Exception as e:
                        # If the detect loss call signature is different, skip gracefully
                        print(f"[WARN] detect loss call failed: {e}. Skipping detection loss for this batch.")
                        loss_obj = torch.tensor(0.0, device=device)
                else:
                    # detect loss unavailable; we skip detection training
                    loss_obj = torch.tensor(0.0, device=device)

            # -------------------------
            # Forward emotion images -> emotion logits
            # -------------------------
            _, emo_logits = model(emo_imgs)  # detection_out (ignored), emotions_logits
            # emo_logits expected shape [B, num_emotions] (depending on multitask_model impl)
            # emo_labels shape [B] with class indices 0..7
            # Some labels may be -1 (no face/label) -> we mask them
            valid_mask = emo_labels >= 0
            if valid_mask.any():
                logits_valid = emo_logits[valid_mask]
                labels_valid = emo_labels[valid_mask]
                loss_emo = criterion_emo(logits_valid, labels_valid)
            else:
                loss_emo = torch.tensor(0.0, device=device)

            # -------------------------
            # Total loss and backward
            # -------------------------
            total_loss = args.w_obj * loss_obj + args.w_emo * loss_emo
            total_loss.backward()
            optimizer.step()

            # Logging
            epoch_loss += float(total_loss.item())
            epoch_emo_loss += float(loss_emo.item()) if isinstance(loss_emo, torch.Tensor) else 0.0
            epoch_obj_loss += float(loss_obj.item()) if isinstance(loss_obj, torch.Tensor) else 0.0
            num_batches += 1

            pbar.set_postfix({
                "tot_loss": f"{(epoch_loss / num_batches):.4f}",
                "emo_loss": f"{(epoch_emo_loss / num_batches):.4f}",
                "obj_loss": f"{(epoch_obj_loss / num_batches):.4f}"
            })

        # End epoch
        avg_loss = epoch_loss / max(1, num_batches)
        avg_emo_loss = epoch_emo_loss / max(1, num_batches)
        avg_obj_loss = epoch_obj_loss / max(1, num_batches)
        print(f"[EPOCH {epoch}] avg_loss={avg_loss:.4f} emo_loss={avg_emo_loss:.4f} obj_loss={avg_obj_loss:.4f}")

        # Save checkpoint
        ckpt_path = os.path.join(args.save_dir, f"multitask_epoch{epoch}.pth")
        torch.save({
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "avg_loss": avg_loss
        }, ckpt_path)
        print(f"[INFO] Checkpoint saved: {ckpt_path}")

    print("[INFO] Training finished.")


if __name__ == "__main__":
    main()
