"""
Purpose: Unzip the manually downloaded IEEE‑CIS Fraud Detection dataset into data/raw/.
"""

# Load requested libraries
import shutil
from pathlib import Path


def extract_ieee_fraud_zip():
    # Resolve project root relative to this script's location
    project_root = Path(__file__).resolve().parents[2]  # src/data/ -> src/ -> project root
    raw_dir = project_root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    # Find the zip file in data/raw/
    zip_files = list(raw_dir.glob("*.zip"))
    if not zip_files:
        raise FileNotFoundError(f"No ZIP file found in: {raw_dir}")

    zip_path = zip_files[0]  # take the first ZIP found
    print(f"Extracting {zip_path.name} to {raw_dir}...")
    shutil.unpack_archive(zip_path, raw_dir)
    print("Extraction complete!")


if __name__ == "__main__":
    extract_ieee_fraud_zip()