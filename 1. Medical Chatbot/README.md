# Medical ChatBot

Ce projet est un chatbot médical intelligent basé sur une architecture **RAG (Retrieval-Augmented Generation)**. Il permet d'extraire des informations précises à partir de documents médicaux (comme le `Medical_book.pdf` fourni) pour répondre aux questions des utilisateurs.

## Fonctionnement du Projet

Le système suit un pipeline de traitement de données complet :

1.  **Extraction de données** (`utils/text_extraction.py`) : Le texte est extrait du fichier PDF médical.
2.  **Prétraitement et Nettoyage** (`utils/preprocessing.py`) : Le texte est nettoyé et découpé en segments.
3.  **Vectorisation et Stockage** (`pinecone/index.py`) : Les segments sont convertis en vecteurs et stockés dans **Pinecone**.
4.  **Interface API** (`api/main.py`) : Un serveur Flask expose un endpoint `/ask` pour interroger le chatbot.
5.  **Interface Utilisateur** (`frontend/streamlit_app.py`) : Une application Streamlit permet de discuter avec le chatbot de manière conviviale.

## Installation et Utilisation

### Prérequis

Définir les variables d'environnement suivantes :
```bash
export PINECONE_API_KEY="votre_cle_pinecone"
export HUGGINGFACEHUB_API_TOKEN="votre_cle_huggingface"
```

### Installation Locale

1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Lancez l'indexation des documents (si nécessaire) :
   ```bash
   python pinecone/index.py
   ```
3. Lancez l'API :
   ```bash
   python api/main.py
   ```
4. Lancez le frontend :
   ```bash
   streamlit run frontend/streamlit_app.py
   ```

### Utilisation avec Docker

Lancez l'ensemble des services avec Docker Compose :
```bash
docker-compose up --build
```
L'interface sera disponible sur `http://localhost:8501`.

## Tests

Pour lancer les tests :
```bash
pytest tests/
```

---

**Structure du Projet**

- `api/` : Serveur Flask (Backend).
- `frontend/` : Application Streamlit (UI).
- `pinecone/` : Scripts de gestion de la base vectorielle.
- `utils/` : Utilitaires de traitement de texte.
- `Data/` : Documents PDF et fichiers de segments/embeddings.
- `tests/` : Tests unitaires.
