"""Load or train ML artifacts for deployment."""

from __future__ import annotations

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from paths import DATASET_PATH, MODEL_PATH, SCALER_PATH


def _load_and_encode_dataset() -> tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv(DATASET_PATH)
    df.columns = df.columns.str.strip()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()

    df["education"] = df["education"].map({"Graduate": 1, "Not Graduate": 0})
    df["self_employed"] = df["self_employed"].map({"Yes": 1, "No": 0})
    df["loan_status"] = df["loan_status"].map({"Approved": 1, "Rejected": 0})
    df.dropna(inplace=True)

    x = df.drop(["loan_id", "loan_status"], axis=1)
    y = df["loan_status"]
    return x, y


def train_and_save_artifacts() -> tuple[LogisticRegression, StandardScaler]:
    """Train model from dataset and persist pickle files."""
    x, y = _load_and_encode_dataset()

    x_train, _, y_train, _ = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)

    model = LogisticRegression(max_iter=2000)
    model.fit(x_train_scaled, y_train)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    return model, scaler


def load_artifacts() -> tuple[LogisticRegression, StandardScaler]:
    """Load pickles; train automatically if missing (Streamlit Cloud friendly)."""
    if not MODEL_PATH.exists() or not SCALER_PATH.exists():
        if not DATASET_PATH.exists():
            raise FileNotFoundError(
                f"Dataset not found at {DATASET_PATH}. "
                "Ensure dataset/loan_data.csv is committed to the repository."
            )
        train_and_save_artifacts()

    return joblib.load(MODEL_PATH), joblib.load(SCALER_PATH)
