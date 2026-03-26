"""
Purpose:
    The purpose of this script is to optimise memory usage for pandas DataFrames.
    It iterates through each numeric column and reduces its data type (dtype) to the smallest possible 
        without losing any information, in order to drastically reduce RAM usage.
"""

# Load requested libraries
import pandas as pd
import numpy as np
import os

# Function to reduce memory usage of a DataFrame
def reduce_mem_usage(df, verbose=True):
    """
    Iterates through columns and downcasts numeric types to save RAM.
    """
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        col_type = df[col].dtype
        
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                else:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**2
    if verbose:
        print(f'Mem. usage decreased to {end_mem:.2f} Mb ({100 * (start_mem - end_mem) / start_mem:.1f}% reduction)')
    return df

def load_and_merge(base_path="data/raw"):
    """
    Loads transaction and identity files and merges them.
    """
    print("Loading Transaction Data...")
    train_trans = pd.read_csv(f"{base_path}/train_transaction.csv")
    train_id = pd.read_csv(f"{base_path}/train_identity.csv")
    
    print("Merging Data...")
    train = pd.merge(train_trans, train_id, on='TransactionID', how='left')
    
    # Clean up memory immediately
    del train_trans, train_id
    
    return reduce_mem_usage(train)