# 🔵 PHASE 1 — Reconnaissance des émotions sur visages (images fixes)

## 1. Spécifications Fonctionnelles

### 🎯 Objectif

Permettre au système d’identifier automatiquement l’émotion affichée sur un visage humain dans une image fixe.

### ✅ Fonctionnalités attendues

- Le système reçoit en entrée une image (JPEG, PNG).
- Le système localise dans l’image un ou plusieurs visages.
- Pour chaque visage détecté :
  - Il extrait la région du visage.
  - Il classe l’expression dans l’une des émotions suivantes :
    **Neutre, Joie, Tristesse, Colère, Peur, Surprise, Dégoût, Mépris** (modifiable).
- Le système renvoie :
  - La position (bounding box) du visage.
  - L’émotion prédite + un score de confiance.
- Le système doit fonctionner sur des images variées (éclairage, angles, âges, ethnies).
- Le système doit pouvoir gérer plusieurs visages sur une même image.

### 📏 Critères d’acceptation

- Détection correcte des visages dans ≥ **90 %** des cas (base de test interne).
- Précision globale du classifieur d’émotion ≥ **75 %** (bases publiques).
- Précision par émotion ≥ **60 %**, sauf classes rares.
- Temps d’inférence sur une image ≤ **300 ms** sur GPU moyen.

---

## 2. Spécifications Techniques

### 🏗️ Architecture

- Détecteur de visages ou détecteur général **YOLO (YOLOv8/YOLOv11)**.
- Classifieur d’émotion séparé basé sur **PyTorch** :
  - CNN (**ResNet18/34**) ou transformer léger (**ViT-tiny**).
- **Pipeline** :
  Image → YOLO (détection visage) → Crop → Emotion Classifier → Output

### 📂 Jeux de données

- **AffectNet**, **RAF-DB**, **FER2013**, **WIDER FACE** (détection visages).

### 🔄 Prétraitements

- Resize → Normalisation **ImageNet**.
- Data augmentation visage : flips, brightness, rotations légères.

### 🏋️ Entraînement

- Détecteur YOLO fine-tuné sur visages.
- Classifieur entraîné via **PyTorch** (cross-entropy).
- Optimiseur : **AdamW** ou **SGD**.

### 📤 Sortie modèle

- **TorchScript** ou **ONNX** pour intégration ultérieure.

---
