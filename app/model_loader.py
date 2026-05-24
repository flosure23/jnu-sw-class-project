import joblib
import mlflow
import mlflow.sklearn

from mlflow.tracking import MlflowClient

from app.config import LOCAL_MODEL_PATH, MLFLOW_TRACKING_URI, MODEL_URI


_model = None
_model_info = None
_model_error = None


def configure_mlflow():
    if MLFLOW_TRACKING_URI:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        mlflow.set_registry_uri(MLFLOW_TRACKING_URI)


def load_model():
    global _model
    global _model_error

    if _model is not None:
        return _model

    try:
        if MODEL_URI and MLFLOW_TRACKING_URI:
            configure_mlflow()
            _model = mlflow.sklearn.load_model(MODEL_URI)
        else:
            _model = joblib.load(LOCAL_MODEL_PATH)

        return _model

    except Exception as e:
        _model_error = str(e)
        raise


def get_model_info():
    global _model_info

    if _model_info is not None:
        return _model_info

    if not MODEL_URI or not MLFLOW_TRACKING_URI:
        _model_info = {
            "run_id": "local",
            "model_type": "local",
            "test_accuracy": None,
            "error": None
        }
        return _model_info

    try:
        configure_mlflow()

        info = mlflow.models.get_model_info(MODEL_URI)
        run = MlflowClient().get_run(info.run_id)

        _model_info = {
            "run_id": info.run_id,
            "model_type": run.data.params.get("model_type"),
            "test_accuracy": run.data.metrics.get("test_accuracy"),
            "error": None
        }

    except Exception as e:
        _model_info = {
            "run_id": "unknown",
            "model_type": "unknown",
            "test_accuracy": None,
            "error": str(e)
        }

    return _model_info


def get_model_error():
    return _model_error