import os
import joblib
import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
ARTIFACT_DIR = os.path.join(BASE_DIR, "artifacts")
MODEL_PATH = os.path.join(ARTIFACT_DIR, "spam_model.joblib")

DATA_PATH = os.path.join(DATA_DIR, "spam.csv")

os.makedirs(ARTIFACT_DIR, exist_ok=True)


MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db")

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_registry_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment("spam-classification-server")


def load_data():
    df = pd.read_csv(DATA_PATH)

    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError("CSV file must contain 'text' and 'label' columns.")

    return df


def train():
    df = load_data()

    X = df["text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.33,
        random_state=42,
        stratify=y
    )

    models = {
        "LogisticRegression": LogisticRegression(max_iter=200),
        "NaiveBayes": MultinomialNB(),
        "DecisionTree": DecisionTreeClassifier(random_state=42)
    }

    for model_name, model in models.items():
        with mlflow.start_run(run_name=model_name):
            pipeline = Pipeline([
                ("vectorizer", CountVectorizer()),
                ("classifier", model)
            ])

            pipeline.fit(X_train, y_train)

            train_preds = pipeline.predict(X_train)
            test_preds = pipeline.predict(X_test)

            train_acc = accuracy_score(y_train, train_preds)
            test_acc = accuracy_score(y_test, test_preds)

            mlflow.log_param("model_type", model_name)
            mlflow.log_param("vectorizer", "CountVectorizer")
            mlflow.log_param("train_data_path", DATA_PATH)
            mlflow.log_param("train_row_count", len(X_train))
            mlflow.log_param("test_row_count", len(X_test))

            mlflow.log_metric("train_accuracy", train_acc)
            mlflow.log_metric("test_accuracy", test_acc)

            joblib.dump(pipeline, MODEL_PATH)

            mlflow.log_artifact(DATA_PATH)
            mlflow.log_artifact(MODEL_PATH)

            mlflow.sklearn.log_model(
                sk_model=pipeline,
                artifact_path="model",
                registered_model_name="spam-model"
            )

            print(f"model: {model_name}")
            print(f"Model saved to: {MODEL_PATH}")
            print(f"train_accuracy: {train_acc:.4f}")
            print(f"test_accuracy: {test_acc:.4f}")


if __name__ == "__main__":
    train()