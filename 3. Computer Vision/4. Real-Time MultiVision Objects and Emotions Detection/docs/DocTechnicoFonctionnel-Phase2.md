# 🟢 PHASE 2 — Détection d’objets + Reconnaissance d’émotions simultanées

## 1. Spécifications Fonctionnelles

### 🎯 Objectif

Créer un système capable d’analyser une image pour :

- Identifier tous les objets visibles (**classes COCO**).
- Identifier les visages dans l’image.
- Reconnaître l’émotion associée à chaque visage.
- Fournir tous les résultats dans une seule prédiction intégrée.

### ✅ Fonctionnalités attendues

- **Entrée** : une image.
- **Sorties** :
  - Liste des objets détectés (**classe + bbox + score**).
  - Liste des visages détectés (**bbox + score**).
  - Pour chaque visage détecté : une émotion (**avec score**).
- Compatible multi-personnes et multi-objets.
- Gestion d’images haute résolution.
- Interfaçable avec une **API** ou script **Python**.

### 📏 Critères d’acceptation

- **mAP (détection objets)** ≥ 0.35 sur COCO subset.
- **Précision émotion** ≥ 70 %.
- Pipeline complet ≤ **400 ms** par image sur GPU.

---

## 2. Spécifications Techniques

### 🏗️ Architecture retenue

Deux options possibles :

#### **Option A — Pipeline Modulaire (recommandé)**

- YOLO pour objets + visages → Crop faces → Classifieur émotion  
  **Avantages :**
- Facile à entraîner.
- Performances élevées.
- Débogage simple.  
  **Inconvénients :**
- Deux modèles = latence un peu plus élevée.

#### **Option B — Modèle Multitâche Unifié (avancé)**

- Modification du détecteur YOLO :
  - Ajout d’une tête secondaire pour l’émotion pour chaque bbox visage détectée.
- Une seule passe = gain en vitesse.  
  **Inconvénients :**
- Plus complexe ; nécessite dataset fusionné (visages + émotions).

---

### 📂 Jeux de données

- **Détection** : COCO, OpenImages.
- **Visages** : WIDER FACE.
- **Émotions** : AffectNet, RAF-DB.
- Fusion des annotations possible (script dédié).

---

### 🏋️ Entraînement

- Fine-tuning YOLO sur **COCO + WIDER FACE**.
- Fine-tuning classifieur émotion séparé (si pipeline modulaire).
- Synchronisation pipeline via **PyTorch/Ultralytics**.

---

### ⚡ Performance & Optimisation

- Batch inference possible.
- Export en **ONNX → TensorRT** pour optimisation.

---

### 📦 Livrables

- Modèle YOLO multitâche ou pipeline YOLO+PyTorch.
- API Python (détection + émotions).
- Notebook d’évaluation multi-métriques.

---
