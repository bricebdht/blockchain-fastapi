"""
APIs related to transactions
"""
from fastapi import APIRouter

from app.models.block_model import Block, Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)


@router.post("/new")
def post(transaction: Transaction) -> Transaction:
    """Create a new transaction in database"""
    last_block = Block.get_last_block()
    last_block["transactions"].append(transaction.dict())
    Block(**last_block).update({"transactions": last_block["transactions"]})

    return f"Transaction has been added to block {last_block['index']}"
