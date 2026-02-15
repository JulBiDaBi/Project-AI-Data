import os
from ultralytics import YOLO

# Définir le chemin HOME
HOME = os.getcwd()

# Charger le modèle YOLOv8 pré-entraîné
model = YOLO("yolov8m.pt")

# Charger la configuration YAML (chemin vers ton fichier YAML)
config = os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format", "data_AffectNet.yaml")

# Entraînement du modèle
results = model.train(
    data=config,            # Fichier YAML
    epochs=100,             # Nombre d'époques
    imgsz=640,              # Taille des images
    batch=16,               # Taille du batch
    device="cpu",           # "cpu" ou "0" pour GPU
    lr0=0.001,              # Taux d'apprentissage initial
    optimizer="Adam",       # Optimiseur
    augment=True,           # Augmentation des données
    project="affectnet_training",  # Dossier projet
    name="yolov8m_emotions_v1"     # Nom de l'expérience
)

# Évaluation automatique sur le set de validation
metrics = model.val()

# Test sur le set test
model.val(split="test")

# Export du modèle au format ONNX
model.export(format="onnx")

# Sauvegarde du modèle entraîné
model_path = os.path.join(HOME, "Phase1_EmotionRecognition", "models", "yolov8m_emotions_affectnet.pt")
os.makedirs(os.path.dirname(model_path), exist_ok=True)
model.save(model_path)

print(f"Modèle sauvegardé sous: {model_path}")