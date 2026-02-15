# PURPOSE: Train a YOLOv8 model for emotion recognition using AffectNet dataset in YOLO format.

import os
import yaml
from ultralytics import YOLO

# 0. Définition du répertoire courant
HOME = os.getcwd()
print(f"Message: Current working directory is set to {HOME}")

# 1. Charger le fichier YAML
data_yaml_path = os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format", "data.yaml")

with open(data_yaml_path, 'r') as file:
    config = yaml.safe_load(file)

# Vérification des chemins
print("✅ Dataset configuration loaded:")
for key in ['train', 'val', 'test']:
    print(f"{key}: {config[key]}")

# 2. Charger un modèle YOLOv8 pré-entraîné
model = YOLO("yolov8m.pt")

# 3. Entraînement
results = model.train(
    data=config,  # On passe le dictionnaire YAML directement
    epochs=100,
    imgsz=640,
    batch=16,
    device="cpu",  # "cpu" ou "0" si GPU disponible
    lr0=0.001,
    optimizer="Adam",
    augment=True,
    project="affectnet_training",
    name="yolov8m_emotions_v1",
)

# 4. Évaluation automatique sur le set de validation
metrics = model.val()

# 5. Test sur le set test
model.val(split="test")

# 6. Export du modèle (ONNX, TorchScript, etc.)
model.export(format="onnx")

# 7. Sauvegarde du modèle entraîné
model_path = os.path.join(HOME, "Phase1_EmotionRecognition", "models", "yolov8m_emotions_affectnet.pt")
model.save(model_path)
print(f"✅ Modèle sauvegardé sous: {model_path}")