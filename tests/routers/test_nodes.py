"""Tests of API regarding nodes"""
from fastapi.testclient import TestClient

from app.main import app
from app.models.node_model import Node

client = TestClient(app)


def test_register_new_node():
    """Register a new node successfully"""
    response = client.post(
        "/nodes/register", json={"address": "http://192.168.0.5:5000"}
    )
    assert response.status_code == 200
    assert response.json() == "Node has been registered"
    assert Node.get_collection().count_documents({}) == 1
