from fastapi.testclient import TestClient

from app.main import app
from app.models.transaction_model import Transaction

client = TestClient(app)


def generate_payload() -> Transaction:
    return {"sender": "toto", "recipient": "titi", "amount": 5}


def test_create_transaction():
    response = client.post("/transactions/new", json=generate_payload())
    assert response.status_code == 200
