# 🔴 PHASE 3 — Traitement en temps réel sur flux vidéo

## 1. Spécifications Fonctionnelles

### 🎯 Objectif

Analyser en direct un flux vidéo (**webcam, caméra IP, vidéo embarquée**) pour détecter :

- Les objets
- Les visages
- Les émotions  
  **Le tout en temps réel.**

### ✅ Fonctionnalités attendues

- **Streaming vidéo depuis :**
  - Webcam USB / laptop
  - Vidéo MP4
  - Flux RTSP (optionnel)
- **Détection en temps réel :**
  - Objets
  - Visages
  - Émotions
- **Affichage en direct avec :**
  - Bounding boxes
  - Labels + scores
- **Sauvegarde optionnelle :**
  - Vidéo annotée
  - JSON par frame
- **API temps réel :**
  - Fonction Python ou service HTTP

### 📏 Critères d’acceptation

- Débit ≥ **15 FPS** (objectif idéal : 25–30 FPS)
- Latence par frame ≤ **80 ms** (sur GPU)
- Stabilité du flux (**0 crash / 1 heure de test**)
- Dégradation limitée en conditions réelles (lumière, angles)

---

## 2. Spécifications Techniques

### 🏗️ Pipeline

    OpenCV (acquisition vidéo)
    → Prétraitements
    → (Option A) YOLO → crop faces → emotion classifier
    → Overlay avec OpenCV
    → Émission / affichage en temps réel

### ⚡ Performances

- Thread de lecture vidéo séparé du thread d’inférence
- Utilisation de **queues FIFO** pour synchroniser
- Optionnel : batching = 1 pour éviter latence

### 🔍 Optimisation obligatoire

- Export YOLO : **ONNX → TensorRT**
- Quantization **INT8** si compatible
- Emotion classifier : version compacte (**MobileNetV3** ou **ResNet18**)
- Pipeline asynchrone (**producer/consumer**)

### 🖥️ Environnements recommandés

- **PC GPU NVIDIA** (RTX 20xx/30xx/40xx)
- Option embarqué : **Jetson Nano / Xavier / Orin** (TensorRT)

### 📚 Frameworks

- **PyTorch** pour entraînement
- **ONNX Runtime / TensorRT** pour inference

---

### 📦 Livrables

- Script `realtime_pipeline.py`
- Interface simple (console, fenêtre OpenCV)
- Export modèle (**ONNX/TensorRT**)
- Manuel utilisateur pour installation et lancement

---
