"""Tests of API regarding mining"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_mine_new_block():
    """Mine a new block successfully"""
    response = client.get("/mine")
    assert response.status_code == 200
    assert response.json()["proof"] == 132668
    assert len(response.json()["transactions"]) == 1
