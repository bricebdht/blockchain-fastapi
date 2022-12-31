"""Tests of API regarding transactions"""
from fastapi.testclient import TestClient

from app.main import app
from app.models.block_model import Block, Transaction

client = TestClient(app)


def generate_payload() -> Transaction:
    """Generate payload used in POST and PUT requests"""
    return {"sender": "toto", "recipient": "tutu", "amount": 5}


def test_create_transaction():
    """Create transaction successfully"""
    response = client.post("/transactions/new", json=generate_payload())
    assert response.status_code == 200

    blocks = list(Block.get_collection().find())
    assert len(blocks[0]["transactions"]) == 1
    assert response.json() == "Transaction has been added to block 0"
