"""Project paths — work locally and on Streamlit Cloud."""

from __future__ import annotations

import sys
from pathlib import Path

# Repo root (folder containing app.py)
PROJECT_ROOT = Path(__file__).resolve().parent

DATASET_PATH = PROJECT_ROOT / "dataset" / "loan_data.csv"
MODEL_PATH = PROJECT_ROOT / "model.pkl"
SCALER_PATH = PROJECT_ROOT / "scaler.pkl"
HAPPY_GIF_PATH = PROJECT_ROOT / "happy_family.gif"
SAD_GIF_PATH = PROJECT_ROOT / "sad_family.gif"


def setup_import_path() -> None:
    """Ensure repo root is on sys.path (helps multipage imports on Cloud)."""
    root = str(PROJECT_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)


setup_import_path()
