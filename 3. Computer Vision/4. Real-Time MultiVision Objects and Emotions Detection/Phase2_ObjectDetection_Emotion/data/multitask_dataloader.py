# Phase2/datasets/multitask_dataloader.py

import os
import glob
import random
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torch
import torchvision.transforms as T


class MultitaskDataset(Dataset):
    """
    Dataset multitâche :
    - Dataset A : détection d’objets/visages (format YOLO)
    - Dataset B : classification des émotions (YOLO AffectNet)
    """

    def __init__(self, 
                 detection_root,
                 emotion_root,
                 img_size=640):
        
        self.detection_imgs = sorted(glob.glob(os.path.join(detection_root, "images", "*.*")))
        self.emotion_imgs = sorted(glob.glob(os.path.join(emotion_root, "images", "*.*")))

        # Transforms
        self.transforms = T.Compose([
            T.Resize((img_size, img_size)),
            T.ToTensor()
        ])

    def __len__(self):
        # On mélange les deux datasets pour un training équitable
        return max(len(self.detection_imgs), len(self.emotion_imgs))

    def load_yolo_label(self, img_path):
        """Charge les labels YOLO (si existent)."""
        label_path = img_path.replace("images", "labels").rsplit(".", 1)[0] + ".txt"
        if not os.path.exists(label_path):
            return torch.zeros((0, 5))  # aucun box
        data = []
        with open(label_path, "r") as f:
            for line in f.readlines():
                values = list(map(float, line.strip().split()))
                data.append(values)
        return torch.tensor(data, dtype=torch.float32)

    def __getitem__(self, idx):
        # ------------------------
        # 1️⃣ Échantillon du dataset détection
        # ------------------------
        det_img = Image.open(self.detection_imgs[idx % len(self.detection_imgs)]).convert("RGB")
        det_img = self.transforms(det_img)
        det_label = self.load_yolo_label(self.detection_imgs[idx % len(self.detection_imgs)])

        # ------------------------
        # 2️⃣ Échantillon du dataset émotions
        # ------------------------
        emo_img = Image.open(self.emotion_imgs[idx % len(self.emotion_imgs)]).convert("RGB")
        emo_img = self.transforms(emo_img)
        emo_label_raw = self.load_yolo_label(self.emotion_imgs[idx % len(self.emotion_imgs)])

        # AffectNet YOLO : cls, x,y,w,h
        # On veut seulement le label émotion (class)
        emotion_class = emo_label_raw[0][0].long() if len(emo_label_raw) > 0 else torch.tensor(-1)

        return {
            "det_img": det_img,
            "det_label": det_label,
            "emo_img": emo_img,
            "emo_label": emotion_class
        }


def collate_fn(batch):
    """
    Permet de regrouper proprement les batchs variés.
    """
    det_imgs = []
    det_labels = []
    emo_imgs = []
    emo_labels = []

    for b in batch:
        det_imgs.append(b["det_img"])
        det_labels.append(b["det_label"])

        emo_imgs.append(b["emo_img"])
        emo_labels.append(b["emo_label"])

    return {
        "det_imgs": torch.stack(det_imgs),
        "det_labels": det_labels,
        "emo_imgs": torch.stack(emo_imgs),
        "emo_labels": torch.tensor(emo_labels)
    }


def get_multitask_loader(detection_root,
                         emotion_root,
                         batch_size=8,
                         img_size=640,
                         shuffle=True,
                         num_workers=2):

    dataset = MultitaskDataset(
        detection_root=detection_root,
        emotion_root=emotion_root,
        img_size=img_size
    )

    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        collate_fn=collate_fn
    )
