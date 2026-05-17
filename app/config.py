# app/config.py
import os

MODEL_MODE = "ml"

LOCAL_MODEL_PATH = "ml/artifacts/spam_model.joblib"

MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"

MODEL_URI = "models:/spam-model@champion"