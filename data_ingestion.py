import pandas as pd
import os

DATA_PATH = r"C:\Users\HP\OneDrive\Desktop\mutual_fund_analytics\data\raw"

files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

for file in files:

    print("\n" + "="*80)
    print("Dataset:", file)

    path = os.path.join(DATA_PATH, file)

    df = pd.read_csv(path)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Records:")
    print(df.head())