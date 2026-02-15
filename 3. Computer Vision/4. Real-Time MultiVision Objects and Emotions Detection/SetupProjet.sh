#!/bin/bash

###############################################
# Script d’installation du projet 
# Real-Time MultiVision Objects and Emotions Detection
# Détection d’émotions + Détection d’objets
# Frameworks : PyTorch + YOLO
# Auteur : JulBiDaBi
###############################################

set -e  # Stoppe le script en cas d’erreur

HOME_DIR="$PWD"
echo "-------------------------------------------"
echo "Current HOME directory is: $HOME_DIR"
echo "-------------------------------------------"

echo "--------------------------------------------------------------------------------"
echo " Initialisation du projet Real-Time MultiVision Objects and Emotions Detection"
echo "--------------------------------------------------------------------------------"

#############################
### 1. Création des dossiers
#############################
echo "Création de la structure de dossiers..."

mkdir -p "$HOME_DIR"

# Dossier communs
mkdir -p Common/{docker,configs,logs,utils,pretrained}

# Documentation Sphinx
mkdir -p docs

# Phase 1 - Détection et reconnaissance des émotions
mkdir -p Phase1_EmotionrRecognition/{data/raw,models,scripts,results}

# Phase 2 - Détection d’objets
mkdir -p Phase2_ObjectDetection/{data/{raw,annotations},models,scripts,results}

# Phase 3 - Pipeline temps réel 
mkdir -p Phase3_RealTime/{models,pipelines,scripts,tests,results}

echo "Structure créée avec succès."


#########################################
### 2. Création d’un environnement Python
#########################################

echo "Création d’un environnement Python (venv)..."

python3 -m venv venv
source venv/Scripts/activate

# Ajout au .gitignore si non présent
if ! grep -q "venv/" "$HOME_DIR/.gitignore" 2>/dev/null; then
    echo "venv/" >> "$HOME_DIR/.gitignore"
fi

echo "Environnement créé et activé."


##################################
### 3. Installation des dépendances
##################################

echo "Installation des dépendances..."

python -m pip install --upgrade pip

# Dépendances projet
pip install pipreqs sphinx sphinx-rtd-theme
pip install numpy pandas matplotlib seaborn ipykernel jupyter opencv-python tqdm pyyaml 

# PyTorch (CUDA auto si compatible)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# YOLO (Ultralytics)
pip install ultralytics

# Annotation + Augmentation
pip install albumentations labelimg fiftyone

# Outils de dev
pip install pytest black isort

echo "Dépendances installées."


############################################
### 3b. Création du fichier requirements.txt
############################################

echo "Génération du fichier requirements.txt..."

pipreqs "$HOME_DIR" --force

echo "Fichier requirements.txt généré."


#################################
### 4. Initialisation de Sphinx
#################################

echo "Initialisation de la documentation Sphinx..."

cd "$HOME_DIR/docs"
sphinx-quickstart --quiet --project "Real-Time MultiVision" --author "JulBiDaBi" --sep

echo "Documentation Sphinx initialisée."

cd "$HOME_DIR"  # Retour dossier racine
