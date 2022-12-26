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
def post(transaction: Transaction) -> Transaction:
    """Create a new transaction in database"""
    transaction.insert()
    return transaction.dict()
