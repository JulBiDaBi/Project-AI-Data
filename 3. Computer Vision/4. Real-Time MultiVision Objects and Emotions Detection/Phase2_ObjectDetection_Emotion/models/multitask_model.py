# Phase2/models/multitask_model.py

import torch
import torch.nn as nn
from ultralytics import YOLO


class MultitaskYOLO(nn.Module):
    """
    Modèle multitâche basé sur YOLOv8 :
    - Tâche 1 : Détection d’objets (ou visages)
    - Tâche 2 : Classification des émotions (8 classes)
    """

    def __init__(self, 
                 detection_model_name="yolov8m.pt",
                 emotion_model_path=None,
                 num_emotions=8,
                 freeze_backbone=False):
        super().__init__()

        # ---------------------------
        # 1️⃣ Charger le modèle YOLO base (backbone + head détection)
        # ---------------------------
        self.detection_yolo = YOLO(detection_model_name).model

        # Extraire le backbone (backbone + neck)
        # Ultralytics : model.model = [backbone, neck, detect head]
        self.backbone = self.detection_yolo.model[0:2]  

        # Détection head
        self.detection_head = self.detection_yolo.model[2]

        # ---------------------------
        # 2️⃣ Charger le modèle émotion pré-entraîné (Phase 1)
        # ---------------------------
        if emotion_model_path is None:
            raise ValueError("Vous devez fournir le chemin du modèle d’émotions YOLOv8 entraîné.")

        emotion_model = YOLO(emotion_model_path).model

        # Retirer la tête YOLO et garder seulement la partie classification fine
        # Son block final est typiquement un Conv => (nc_outputs)
        self.emotion_head = nn.Sequential(
            nn.Conv2d(in_channels=emotion_model.model[2].m[0].conv.out_channels,
                      out_channels=num_emotions,
                      kernel_size=1),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten()
        )

        # ---------------------------
        # 3️⃣ Optional : geler le backbone
        # ---------------------------
        if freeze_backbone:
            for p in self.backbone.parameters():
                p.requires_grad = False

    # ---------------------------------------------------
    # FORWARD MULTITÂCHE
    # ---------------------------------------------------
    def forward(self, x):
        """
        Entrée :
            x -> image (batch)
        Sorties :
            - detection_out
            - emotions_logits
        """

        # Backbone -> features
        features = self.backbone(x)

        # Head détection YOLOv8
        detection_out = self.detection_head(features)

        # Head émotions
        emotions_logits = self.emotion_head(features[-1])  # dernier niveau du FPN

        return detection_out, emotions_logits
