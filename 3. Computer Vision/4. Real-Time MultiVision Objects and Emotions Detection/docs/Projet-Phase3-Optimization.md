# 🚀 PHASE 3 — Optimisation et Déploiement Temps Réel

Cette phase vise à transformer le pipeline de la Phase 2 en une application fluide capable de traiter des flux vidéo à plus de 30 FPS.

## 1. Stratégies d'Optimisation

### ⚙️ Export vers ONNX et TensorRT
L'utilisation de PyTorch brut pour l'inférence est souvent trop lente pour le temps réel.
- **Action** : Exporter les modèles YOLOv8 au format `.onnx`.
- **Action** : Utiliser **TensorRT** (pour GPU NVIDIA) ou **OpenVINO** (pour CPU Intel) pour accélérer l'inférence.
- **Gain attendu** : Réduction de la latence de 50% à 80%.

### 📉 Quantification (INT8)
La réduction de la précision des poids du modèle (de FP32 à INT8) permet une exécution beaucoup plus rapide sur le matériel compatible.
- **Action** : Calibration post-entraînement pour la quantification INT8.

### 🧩 Pipeline Asynchrone
Pour éviter que le traitement d'une image ne bloque la lecture de la suivante :
- **Action** : Implémenter un système de files d'attente (Queues) pour la lecture vidéo, le traitement IA et l'affichage.

## 2. Choix du Modèle "Edge"
Si `yolov8m.pt` est trop lourd pour la machine cible :
- Passer à `yolov8n.pt` (Nano) ou `yolov8s.pt` (Small).
- Le modèle d'émotions peut également être distillé vers une version plus légère.

## 3. Interface de Déploiement
- **Option 1** : Script OpenCV simple avec affichage `cv2.imshow`.
- **Option 2** : Application **Streamlit** avec support WebRTC pour le streaming navigateur.

## 4. Prochaines étapes immédiates
1.  Évaluer les FPS actuels sur un fichier vidéo avec le script `inference_multivision.py`.
2.  Script de conversion YOLO -> ONNX.
3.  Développement du wrapper d'inférence asynchrone.
