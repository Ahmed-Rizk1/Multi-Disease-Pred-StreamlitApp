import pickle
import os
from pathlib import Path

MODELS_DIR = Path(__file__).parent.parent.parent / "models"


def load_model(model_name: str):
    """Load a saved model from the models directory."""
    model_path = MODELS_DIR / model_name
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")

    with open(model_path, "rb") as f:
        return pickle.load(f)


def get_diabetes_model():
    """Load diabetes prediction model."""
    return load_model("diabetes_model.sav")


def get_heart_disease_model():
    """Load heart disease prediction model."""
    return load_model("heart_disease_model.sav")


def get_parkinsons_model():
    """Load Parkinson's disease prediction model."""
    return load_model("parkinsons_model.sav")
