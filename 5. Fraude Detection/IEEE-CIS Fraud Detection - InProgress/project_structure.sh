#!/bin/bash

# Ensure we are in the project root
echo "🏗️  Initializing IEEE-CIS Fraud Detection MLOps Structure..."

# 1. Create Folder Hierarchy
mkdir -p config
mkdir -p data/{raw,processed,external}
mkdir -p docker
mkdir -p experiments/notebooks
mkdir -p models/{artifacts,encoders}
mkdir -p src/{data,features,models,utils}
mkdir -p tests
mkdir -p submissions
mkdir -p logs

# 2. Create Core Python Files (__init__ makes them importable modules)
touch src/__init__.py
touch src/data/__init__.py
touch src/features/__init__.py
touch src/models/__init__.py
touch src/utils/__init__.py
touch tests/__init__.py

# 3. Create Specific Script Placeholders
touch src/data/loader.py
touch src/data/validator.py
touch src/features/processor.py
touch src/models/trainer.py
touch src/pipeline.py
touch src/utils/logger.py

# 4. Create Configuration & Docker Files
touch config/params.yaml
touch config/logging.conf
touch docker/Dockerfile
touch docker/docker-compose.yml
touch docker/entrypoint.sh

# 5. Create Root Level Files
touch requirements.txt
touch Makefile
touch README.md
touch pyproject.toml

# 6. Pre-populate .gitignore
cat <<EOT >> .gitignore
# Data and Models
data/raw/*
data/processed/*
models/artifacts/*
models/encoders/*

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.venv/
venv/

# IDE & OS
.vscode/
.idea/
.DS_Store

# Experiments
experiments/mlruns/
.ipynb_checkpoints/
EOT

# 7. Pre-populate .dockerignore
cat <<EOT >> .dockerignore
data/
models/artifacts/
experiments/
.git
.gitignore
__pycache__
*.ipynb
EOT

# 8. Pre-populate basic requirements.txt
cat <<EOT >> requirements.txt
pandas
numpy
scikit-learn
lightgbm
xgboost
catboost
pyarrow
