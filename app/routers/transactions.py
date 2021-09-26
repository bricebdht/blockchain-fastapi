"""
APIs related to transactions
"""
from fastapi import APIRouter

from app.models.transaction_model import Transaction

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)


@router.post("/new")
def post(transaction: Transaction) -> None:
    """Create a new transaction in database"""
    print(transaction)
    return "Add transaction"
