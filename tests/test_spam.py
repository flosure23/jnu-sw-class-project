from app.spam import check_spam_rules, check_spam_ml


def test_check_spam_rules_basic():
    assert check_spam_rules("hello")[0] == "ham"
    assert check_spam_rules("free prize click")[0] == "spam"


def test_check_spam_rules_empty():
    assert check_spam_rules("") == ("ham", 0)


def test_check_spam_ml_can_predict():
    label, score = check_spam_ml("free prize click now")
    assert label in ["spam", "ham"]
    assert isinstance(score, float)