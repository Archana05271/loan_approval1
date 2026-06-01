"""Shared dataset loading and project statistics."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from paths import DATASET_PATH

FEATURE_COUNT = 11
MODEL_NAME = "Logistic Regression"


@st.cache_data
def load_loan_dataset() -> pd.DataFrame:
    """Load and clean the loan approval dataset."""
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATASET_PATH}. "
            "Ensure dataset/loan_data.csv is in the repository."
        )

    df = pd.read_csv(DATASET_PATH)
    df.columns = df.columns.str.strip()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()

    return df


@st.cache_data
def get_project_stats() -> dict:
    """Return real statistics from the loan dataset for the Home page."""
    df = load_loan_dataset()
    approved = (df["loan_status"] == "Approved").sum()
    total = len(df)

    return {
        "total_records": total,
        "approved_count": int(approved),
        "rejected_count": int(total - approved),
        "approval_rate": round(approved / total * 100, 1) if total else 0.0,
        "feature_count": FEATURE_COUNT,
        "avg_cibil": round(df["cibil_score"].mean(), 0),
    }
