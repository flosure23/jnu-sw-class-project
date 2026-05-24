import os


MODEL_MODE = os.getenv("MODEL_MODE", "rules")

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "")
MODEL_URI = os.getenv("MODEL_URI", "models:/spam-model@champion")

LOCAL_MODEL_PATH = os.path.join("ml", "artifacts", "spam_model.joblib")