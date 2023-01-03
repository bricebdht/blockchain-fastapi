"""Tests of API regarding nodes"""
from typing import Dict

import requests
from fastapi import status
from fastapi.testclient import TestClient
from pytest import MonkeyPatch

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


class ChainResponse:
    status_code = status.HTTP_200_OK

    @staticmethod
    def json() -> Dict:
        return [
            {
                "index": 0,
                "timestamp": "",
                "transactions": [],
                "proof": 0,
                "previous_hash": None,
            },
            {
                "index": 1,
                "timestamp": "",
                "transactions": [],
                "proof": 0,
                "previous_hash": None,
            },
        ]


def test_resolve_chain(monkeypatch: MonkeyPatch):
    """Resolving the blockchain"""

    def mock_get(self):
        return ChainResponse

    monkeypatch.setattr(requests, "get", mock_get)

    response = client.get(
        "/nodes/resolve",
    )
    assert response.status_code == 200
    assert response.json() == "Node has been registered"
    assert Node.get_collection().count_documents({}) == 1
