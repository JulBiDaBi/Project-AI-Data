"""
Purpose: Create kaggle.json file with Kaggle API credentials to enable downloading datasets directly from Kaggle.
"""

# Load requested libraries
import os
from dotenv import load_dotenv
from pathlib import Path
import json

load_dotenv()

username = os.getenv("KAGGLE_USERNAME")
key = os.getenv("KAGGLE_KEY")

kaggle_dir = Path.home() / ".kaggle"
kaggle_dir.mkdir(exist_ok=True)

with open(kaggle_dir / "kaggle.json", "w") as f:
    json.dump({"username": username, "key": key}, f)

print("kaggle.json created successfully")
