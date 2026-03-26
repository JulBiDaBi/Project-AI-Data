# Load requested libraries
import pandas as pd
import logging


# Basic data validation checks
def validate_data(df):
    """Basic checks to ensure data integrity."""
    required_cols = ['TransactionID', 'isFraud', 'TransactionDT', 'TransactionAmt']
    
    # 1. Check for required columns
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing critical column: {col}")
            
    # 2. Check for empty dataframe
    if df.empty:
        raise ValueError("Dataframe is empty!")

    # 3. Check target balance (Fraud is rare, should be ~3.5%)
    fraud_rate = df['isFraud'].mean() * 100
    logging.info(f"Target distribution: {fraud_rate:.2f}% fraud cases.")
    
    return True


# Split data into train and validation sets based on time
def time_based_split(df, train_prop=0.80):
    """
    Splits the dataframe based on the chronological order of TransactionDT.
    """
    # Ensure data is sorted by time
    df = df.sort_values('TransactionDT')
    
    # Calculate split point
    split_idx = int(len(df) * train_prop)
    
    train_df = df.iloc[:split_idx]
    val_df = df.iloc[split_idx:]
    
    print(f"Train Shape: {train_df.shape} | Val Shape: {val_df.shape}")
    print(f"Train Time Range: {train_df['TransactionDT'].min()} to {train_df['TransactionDT'].max()}")
    print(f"Val Time Range: {val_df['TransactionDT'].min()} to {val_df['TransactionDT'].max()}")
    
    return train_df, val_df