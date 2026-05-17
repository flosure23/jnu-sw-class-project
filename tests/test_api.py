from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_classify_api_contract():
    r = client.post("/classify", json={"text": "hello"})
    assert r.status_code == 200

    data = r.json()
    assert "label" in data
    assert "score" in data
    assert data["label"] in ["spam", "ham"]


def test_classify_api_spam_request():
    r = client.post("/classify", json={"text": "free prize click"})
    assert r.status_code == 200

    data = r.json()
    assert "label" in data
    assert "score" in data