# Load requested libraries
import os
from .data.loader import load_and_merge  


# Main function to run the data preparation pipeline
def run_data_prep():
    # 1. Load and Optimize
    df = load_and_merge("data/raw")
    
    # 2. Save as Parquet
    output_path = "data/processed/train_combined.parquet"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"Saving to {output_path}...")
    df.to_parquet(output_path, engine='pyarrow')
    print("Step 1 Complete: Data is ready and optimized!")


if __name__ == "__main__":
    run_data_prep()