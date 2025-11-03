import os
from datetime import datetime
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

DATA_PATH = "../data/processed"
MODEL_PATH = "../model"
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

os.makedirs(MODEL_PATH, exist_ok=True)

all_csv=[os.path.join(DATA_PATH, f) for f in os.listdir(DATA_PATH) if f.endswith(".csv")]
df_list = [pd.read_csv(f) for f in all_csv]
df = pd.concat(df_list, ignore_index=True)

timestamps_sales = pd.to_datetime(df['Timestamp'], format="%Y%m%d_%H%M")
X = ((timestamps_sales - pd.Timestamp("1970-01-01")) / pd.Timedelta(minutes=1)).values.reshape(-1, 1)
X = X.values.reshape(-1, 1)
y = df['Sales'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(y_test - y_pred))
r2 = r2_score(y_test, y_pred)

first_model_path = os.path.join(MODEL_PATH, "model.pkl")
if not os.path.exists(first_model_path):
    joblib.dump(model, first_model_path)
else:
    later_model_path = os.path.join(MODEL_PATH, f"model_{timestamp}.pkl")
    joblib.dump(model, later_model_path)

model_msg= f"[{timestamp}] R^2: {r2:.4f}, RMSE: {rmse:.4f}, MAE: {mae:.4f}\n"
print(model_msg)
