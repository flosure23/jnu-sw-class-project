from app.spam import check_spam


def test_check_spam_basic():
    assert check_spam("hello")[0] == "ham"
    assert check_spam("free prize click")[0] == "spam"


def test_check_spam_empty():
    assert check_spam("") == ("ham", 0)


def test_check_spam_score():
    label, score = check_spam("free bonus offer")
    assert label == "spam"
    assert score >= 2