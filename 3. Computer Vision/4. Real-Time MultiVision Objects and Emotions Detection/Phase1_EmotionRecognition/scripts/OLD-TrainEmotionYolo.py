# # PURPOSE: This script trains a YOLOv8 model for emotion recognition using the AffectNet dataset in YOLO format.
# print(
#     "**************************************************************************\n"
#     "Training a YOLOv8 model for emotion recognition using the AffectNet dataset in YOLO format.\n"
#     "**************************************************************************"
# )

import os
import yaml
from ultralytics import YOLO

# 0. Définition des paramètres
# a. Define current working directory
HOME = os.getcwd()
print(f"Message: Current working directory is set to {HOME}")

# 1. Charger le YAML
data_yaml_path = os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format", "data.yaml")

with open(data_yaml_path, 'r') as file:
    config = yaml.safe_load(file) 
    
# Remplacer les variables d'environnement dans les chemins
for key in ['train', 'val', 'test', 'data']:
    if HOME in config[key]:
        config[key] = config[key].replace("${MY_ENV_HOME}", HOME)

# 2. Charger un modèle YOLOv8 pré-entraîné
model = YOLO("yolov8m.pt")

# 3. Entraînement
results = model.train(
    data=config
    # data=os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format", "data.yaml"),
    epochs=100,
    imgsz=640,
    batch=16,
    device="cpu",  # Utiliser "0" pour GPU ou "cpu" pour CPU
    lr0=0.001,           # learning rate
    optimizer="Adam",    # optimiser
    augment=True,   # activer les augmentations par défaut
    project="affectnet_training",
    name="yolov8m_emotions_v1",
)

# 3. Évaluation automatique sur le set de validation
metrics = model.val()

# 4. Test sur le set test
model.val(split="test")

# 5. Export du modèle (ONNX, TorchScript, etc.)
model.export(format="onnx")

# 6. Sauvegarde du modèle entraîné
model_path = os.path.join(HOME, "Phase1_EmotionRecognition", "models", "yolov8m_emotions_affectnet.pt")
model.save(model_path)
print(f"Modèle sauvegardé sous: {model_path}")