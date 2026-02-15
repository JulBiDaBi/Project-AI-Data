## **Description du projet**

Le projet consiste à développer un **système multitâche basé sur l’IA** capable de traiter des flux vidéo en temps réel pour deux objectifs principaux :

1.  **Reconnaissance des émotions faciales** : identifier et classifier les émotions exprimées sur les visages (ex. joie, colère, tristesse).
2.  **Détection et reconnaissance d’objets** : localiser et identifier des objets génériques dans la scène (similaire aux modèles YOLO ou DETR).

L’architecture devra être **optimisée pour la performance en temps réel**, garantissant une **latence faible** et un **nombre d’images par seconde (FPS) élevé**, afin de fonctionner efficacement sur des vidéos en streaming.

---

### **Caractéristiques clés**

- **Multitâche** : un seul pipeline pour la détection d’objets et la reconnaissance des émotions.
- **Compatibilité** : traitement d’images statiques et de flux vidéo.
- **Précision et rapidité** : équilibre entre exactitude des prédictions et vitesse d’inférence.

---

### **Approche technique envisagée**

- **Architecture** : backbone partagé (CNN ou Transformer) avec deux têtes spécialisées (objets et émotions), ou pipeline modulaire (détecteur d’objets + classifieur d’émotions).
- **Datasets** : combiner des jeux de données pour la détection d’objets (ex. COCO) et pour les émotions faciales (ex. FER2013, AffectNet).
- **Optimisation temps réel** : quantization, pruning, modèles légers (YOLO-nano, MobileNet), export ONNX/TensorRT pour déploiement sur GPU ou edge devices.

---

### **Roadmap**

1.  **Phase 1** : entraînement d’un modèle de reconnaissance d’émotions sur images.
2.  **Phase 2** : intégration avec un détecteur d’objets pour créer une architecture multitâche.
3.  **Phase 3** : optimisation et déploiement pour flux vidéo en temps réel.

---

### **Livrables attendus**

- Spécifications techniques détaillées (datasets, métriques, hardware).
- Scripts d’entraînement et pipeline de préparation des données.
- Modèle multitâche exporté pour inference rapide.
- Code d’inférence temps réel (OpenCV + ONNX/TorchScript).

---
