def check_spam(text: str):
    # 전처리: 소문자화 및 공백 제거
    text = text.lower().strip()

    if text == "":
        return "ham", 0

    spam_keywords = [
    "free", "win", "winner", "prize", "click",
    "buy now", "urgent", "cash", "money", "offer", "deal",
    "bonus", "limited", "guarantee", "congratulations", "bonus"
    ]

    hit = 0
    for kw in spam_keywords:
        if kw in text:
            hit += 1

    return ("spam", hit) if hit >= 2 else ("ham", hit)