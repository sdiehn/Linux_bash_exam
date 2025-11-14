import pandas as pd
import numpy as np
import os

DATA_PATH="../data/raw"

raw_folder = []
for file in os.listdir(DATA_PATH):
    if file.endswith(".csv"):
        raw_folder.append(file)

latest_file = max(raw_folder, key=lambda x: os.path.getctime(os.path.join(DATA_PATH, x)))
latest_file_path = os.path.join(DATA_PATH, latest_file)
df = pd.read_csv(latest_file_path)
df_cleaned = df.dropna()
df_cleaned = df_cleaned[df_cleaned['sales'] >= 0]
df_cleaned = df_cleaned[df_cleaned['sales'] % 1 == 0]

timestamp_sales = pd.to_datetime(df_cleaned['timestamp'].iloc[0], format="%Y%m%d_%H%M")
X = ((timestamp_sales - pd.Timestamp("1970-01-01")) / pd.Timedelta(minutes=1))
df_grouped = df_cleaned.groupby('timestamp', as_index=False)['sales'].sum()

y = df_grouped['sales']

df_xy = pd.DataFrame({
    "X": int(X),
    "y": y.values.astype(int)
})

print(df_xy.to_csv(index=False))