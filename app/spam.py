# app/spam.py
from app.model_loader import load_model


def check_spam_rules(text: str):
    text = text.lower().strip()

    if text == "":
        return "ham", 0

    spam_keywords = [
        "free", "win", "winner", "prize", "click",
        "buy now", "urgent", "cash", "money", "offer", "deal",
        "bonus", "limited", "guarantee", "congratulations"
    ]

    hit = 0
    for kw in spam_keywords:
        if kw in text:
            hit += 1

    label = "spam" if hit > 0 else "ham"
    return label, hit


def check_spam_ml(text: str):
    text = text.strip()

    if text == "":
        return "ham", 0.0

    model = load_model()

    pred = model.predict([text])[0]

    if hasattr(model, "predict_proba"):
        proba = model.predict_proba([text])[0]
        classes = list(model.classes_)
        pred_index = classes.index(pred)
        score = float(proba[pred_index])
    else:
        score = 1.0

    return pred, score


# 기존 테스트와 API 호환을 위해 check_spam 이름 유지
def check_spam(text: str):
    return check_spam_ml(text)