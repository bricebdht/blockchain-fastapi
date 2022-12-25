"""
APIs related to transactions
"""
from fastapi import APIRouter
from pymongo import MongoClient

from app.models.transaction_model import Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)

client = MongoClient(host="localhost", port=27017)


@router.post("/new")
def post(transaction: Transaction) -> None:
    """Create a new transaction in database"""
    client.blockchain.transaction.insert_one(transaction.dict())
    for data in client.blockchain.transaction.find():
        print(data)
    return "Add transaction"
