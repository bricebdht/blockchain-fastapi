from app.models.transaction_model import Transaction
from fastapi import APIRouter

router = APIRouter()


@router.post("/transactions/new")
def post(transaction: Transaction) -> None:
    return "Add transaction"
