from app.config import MODEL_MODE
from app.model_loader import load_model


SPAM_WORDS = [
    "free",
    "prize",
    "winner",
    "win",
    "cash",
    "urgent",
    "click",
    "offer",
    "claim",
    "money",
    "reward",
    "verify",
    "payment",
    "account"
]


def check_spam_rules(text: str):
    clean_text = text.strip()

    if not clean_text:
        return "ham", 0.0

    lowered = clean_text.lower()
    hit_count = sum(1 for word in SPAM_WORDS if word in lowered)

    if hit_count > 0:
        score = min(0.5 + hit_count * 0.1, 0.99)
        return "spam", score

    return "ham", 0.5


def check_spam_ml(text: str):
    clean_text = text.strip()

    if not clean_text:
        return "ham", 0.0

    model = load_model()
    label = model.predict([clean_text])[0]

    score = 0.0
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba([clean_text])[0]
        classes = list(model.classes_)

        if label in classes:
            score = float(probabilities[classes.index(label)])

    return label, score


def classify_text(text: str):
    if MODEL_MODE == "mlflow":
        return check_spam_ml(text)

    return check_spam_rules(text)