import torch
import cv2
import numpy as np
import os
from ultralytics import YOLO

def run_inference(img_path):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Chemins des modèles
    obj_model_path = "yolov8m.pt"
    emo_model_path = "Phase1_EmotionRecognition/models/yolov8m_emotions_affectnet.pt"

    if not os.path.exists(obj_model_path) or not os.path.exists(emo_model_path):
        print("Erreur: Modèles introuvables.")
        return

    # Chargement des deux modèles séparément (Option A - Pipeline Modulaire)
    print(f"Chargement des modèles sur {device}...")
    model_obj = YOLO(obj_model_path)
    model_emo = YOLO(emo_model_path)

    # Inférence
    print(f"Analyse de l'image: {img_path}")
    results_obj = model_obj(img_path, device=device, verbose=False)
    results_emo = model_emo(img_path, device=device, verbose=False)

    # Fusion des résultats
    img = cv2.imread(img_path)

    print("\n--- RÉSULTATS MULTIVISION ---")

    # Objets COCO
    print("\n[Objets et Personnes (COCO)]")
    for r in results_obj:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model_obj.names[cls]
            conf = float(box.conf[0])
            print(f"- {label}: {conf:.2%}")

            # Dessiner
            b = box.xyxy[0].cpu().numpy().astype(int)
            cv2.rectangle(img, (b[0], b[1]), (b[2], b[3]), (255, 0, 0), 2)
            cv2.putText(img, f"{label} {conf:.2f}", (b[0], b[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Émotions (Faces)
    print("\n[Émotions Faciales]")
    for r in results_emo:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model_emo.names[cls]
            conf = float(box.conf[0])
            print(f"- Émotion {label}: {conf:.2%}")

            # Dessiner
            b = box.xyxy[0].cpu().numpy().astype(int)
            cv2.rectangle(img, (b[0], b[1]), (b[2], b[3]), (0, 255, 0), 2)
            cv2.putText(img, f"Emo: {label}", (b[0], b[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Sauvegarder le résultat
    output_path = "result_multivision.jpg"
    cv2.imwrite(output_path, img)
    print(f"\nImage résultante sauvegardée sous: {output_path}")

if __name__ == "__main__":
    test_img = "Phase1_EmotionRecognition/data/check_model_images/img1.jpeg"
    if os.path.exists(test_img):
        run_inference(test_img)
    else:
        print(f"Image test non trouvée à {test_img}")
