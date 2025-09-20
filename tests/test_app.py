import json
from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_prediction():
    client = app.test_client()
    res = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    data = res.get_json()
    assert "prediction" in data
