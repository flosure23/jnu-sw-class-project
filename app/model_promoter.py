import mlflow
from mlflow.tracking import MlflowClient

from app.config import MLFLOW_TRACKING_URI


MODEL_NAME = "spam-model"


def _configure_mlflow():
    if MLFLOW_TRACKING_URI:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        mlflow.set_registry_uri(MLFLOW_TRACKING_URI)


def get_champion_test_accuracy(client: MlflowClient) -> float:
    try:
        champion = client.get_model_version_by_alias(MODEL_NAME, "champion")
        champion_run = client.get_run(champion.run_id)
        return float(champion_run.data.metrics.get("test_accuracy", -1.0))
    except Exception:
        return -1.0


def promote_if_better(new_version: str, new_test_accuracy: float) -> None:
    _configure_mlflow()

    client = MlflowClient()
    current_champion_acc = get_champion_test_accuracy(client)

    print(f"[PROMOTION] current champion test_accuracy = {current_champion_acc}")
    print(f"[PROMOTION] new candidate test_accuracy = {new_test_accuracy}")

    if new_test_accuracy > current_champion_acc:
        client.set_registered_model_alias(
            name=MODEL_NAME,
            alias="champion",
            version=str(new_version)
        )
        print(f"[PROMOTION] version {new_version} promoted to champion")
    else:
        print("[PROMOTION] champion unchanged")