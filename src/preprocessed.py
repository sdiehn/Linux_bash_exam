import pandas as pd
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
df_cleaned = df_cleaned[df_cleaned['Sales'] >= 0]
df_cleaned = df_cleaned[df_cleaned['Sales'] % 1 == 0]

print(df_cleaned.to_csv(index=False))
