import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Sample passenger data
sample_passenger = {
    "Pclass": 1,
    "Sex": "female",
    "Age": 30,
    "SibSp": 0,
    "Parch": 0,
    "Fare": 100.0,
    "Embarked": "S"
}

def test_rest_prediction():
    response = client.post("/predict", json=sample_passenger)
    assert response.status_code == 200
    assert "survived" in response.json()
    assert isinstance(response.json()["survived"], bool)
