"""
APIs related to transactions
"""
from fastapi import APIRouter
from pymongo import MongoClient

from app.models.block_model import Block, Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)

client = MongoClient(host="localhost", port=27017)


@router.post("/new")
def post(transaction: Transaction) -> Transaction:
    """Create a new transaction in database"""
    cursor = Block.get_collection().find().sort("_id", -1).limit(1)
    current_block = cursor.next()
    current_block["transactions"].append(transaction.dict())
    Block(**current_block).update({"transactions": current_block["transactions"]})
    return f"Transaction has been added to block ${current_block['_id']}"
