# Classification d'Imagerie Médicale - Tumeurs Cérébrales

Ce projet vise à développer un modèle de Deep Learning capable de classifier automatiquement les tumeurs cérébrales à partir d'images IRM.

## Objectif

L'objectif est de classifier les images en quatre catégories :
- Gliome
- Méningiome
- Pas de tumeur
- Tumeur hypophysaire

## Méthodologie

- **Architecture** : Réseau de neurones convolutifs (CNN).
- **Données** : Utilisation de datasets provenant de Kaggle (Brain Tumor MRI Dataset).
- **Prétraitement** : Redimensionnement, normalisation et augmentation des données (rotation, flip).
- **Évaluation** : Utilisation de la matrice de confusion, du score F1 et de la précision.

## Structure

Le notebook `Project_Classification_Imagerie médicale.ipynb` contient l'intégralité du pipeline, de l'exploration des données à l'évaluation du modèle.
