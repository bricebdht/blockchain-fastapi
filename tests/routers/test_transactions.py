from app.main import app
from fastapi import FastAPI
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_transaction():
    response = client.post("/transactions/new")
    assert response.status_code == 200
