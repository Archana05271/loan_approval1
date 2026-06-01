"""Train and save model.pkl / scaler.pkl locally (optional before deploy)."""

import joblib
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from model_loader import _load_and_encode_dataset, train_and_save_artifacts
from paths import MODEL_PATH, SCALER_PATH


def main() -> None:
    x, y = _load_and_encode_dataset()

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    train_and_save_artifacts()

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    x_test_scaled = scaler.transform(x_test)
    y_pred = model.predict(x_test_scaled)

    print("✅ Model training completed")
    print(f"🎯 Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\n📊 Classification report:\n")
    print(classification_report(y_test, y_pred))
    print(f"✅ Saved {MODEL_PATH.name} and {SCALER_PATH.name}")


if __name__ == "__main__":
    main()
