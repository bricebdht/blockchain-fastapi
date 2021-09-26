from app.models.transaction_model import Transaction
from fastapi import APIRouter

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)


@router.post("/new")
def post(transaction: Transaction) -> None:
    return "Add transaction"
