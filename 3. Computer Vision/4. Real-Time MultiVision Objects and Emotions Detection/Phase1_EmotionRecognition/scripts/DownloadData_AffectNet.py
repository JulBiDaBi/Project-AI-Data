# PURPOSE: This script unzips the AffectNet dataset into the appropriate directory for further processing.
print(
    "**************************************************************************\n"
    "The scripts import AffectNet dataset and unzip it into the 'data/raw_data/AffectNet' directory.\n"
    "**************************************************************************"
)

# 1. Setup Configuration
# 1.1. Load requested libraries
import zipfile 
import os
 
# 1.2. Define parameters
# Define current working directory
HOME = os.getcwd()
print(f"Message: Current working directory is set to {HOME}")
 
DATASET_NAME = "AffectNet"

# 2. Unzip Dataset
zip_path = os.path.join(HOME, "Phase1_EmotionRecognition", "data", "raw", f"{DATASET_NAME}.zip")

# 3. Extract files to the desired directory
destination_dir =  os.path.join(HOME, "Phase1_EmotionRecognition", "data")
os.makedirs(destination_dir, exist_ok=True)

# Unzip the dataset
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(destination_dir)

print(f"Message: {DATASET_NAME} dataset unzipped successfully at {destination_dir}")

# 4. Quick Check: Cardinality of extracted files
print("\nCardinality of extracted files:")

def count_files_in_directory(path):
    """Count files in a given directory."""
    return len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

# List of directories to check
directories = [
    os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format", "valid", "images"),
    os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format", "train", "images"),
    os.path.join(HOME, "Phase1_EmotionRecognition", "data", "YOLO_format", "test", "images")
]

# Affichage des résultats
sets = ["Train", "Test", "Valid"]

for dir_path, set_name in zip(directories, sets):
    file_count = count_files_in_directory(dir_path)
    print(f"Message: {set_name} --> {file_count} fichiers")
 

# END OF SCRIPT