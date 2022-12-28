"""Tests of API regarding transactions"""
from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app
from app.models.block_model import Block, Transaction

client = TestClient(app)


def generate_payload() -> Transaction:
    """Generate payload used in POST and PUT requests"""
    return {"sender": "toto", "recipient": "tutu", "amount": 5}


def test_create_transaction():
    """Create transaction successfully"""
    Block.get_collection().drop()
    new_block = Block(
        index=0,
        timestamp=datetime.now(),
        transactions=[],
    )
    new_block.insert()
    cursor = Block.get_collection().find()
    response = client.post("/transactions/new", json=generate_payload())
    assert response.status_code == 200
    cursor = Block.get_collection().find()
    block = cursor.next()
    assert len(block["transactions"]) == 1
