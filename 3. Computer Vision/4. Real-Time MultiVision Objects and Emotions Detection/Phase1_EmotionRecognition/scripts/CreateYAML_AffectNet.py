import os
import yaml

# Récupérer le chemin courant
HOME = os.getcwd()

# Construire le contenu YAML
data_yaml = {
    "path": os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format"),
    "train": "train/images",
    "val": "valid/images",
    "test": "test/images",
    "nc": 8,
    
    "names": {
        0: "Anger",
        1: "Contempt",
        2: "Disgust",
        3: "Fear",
        4: "Happy",
        5: "Neutral",
        6: "Sad",
        7: "Surprise"
    }
}

# Sauvegarder dans un fichier
file_path = os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format", "data_AffectNet.yaml")
with open(file_path, "w") as f:
    yaml.dump(data_yaml, f)
    
print(f"Fichier YAML sauvegardé à : {file_path}")