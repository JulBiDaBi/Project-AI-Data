# """
# Purpose: Download IEEE‑CIS Fraud Detection data into data/raw/ using kagglehub.
# """

# import kagglehub
# import shutil
# from pathlib import Path
# from dotenv import load_dotenv

# load_dotenv()  # loads KAGGLE_USERNAME and KAGGLE_KEY


# def download_ieee_fraud_data():
#     raw_dir = Path("data/raw")
#     raw_dir.mkdir(parents=True, exist_ok=True)

#     archive_path = kagglehub.competition_download("ieee-fraud-detection")
#     shutil.unpack_archive(archive_path, raw_dir)


# if __name__ == "__main__":
#     download_ieee_fraud_data()


import os
from pathlib import Path
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

def download_ieee_fraud_data():
    # Load .env variables into the OS environment
    load_dotenv()

    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    api.competition_download_files(
        "ieee-fraud-detection",
        path=raw_dir
    )

if __name__ == "__main__":
    download_ieee_fraud_data()
