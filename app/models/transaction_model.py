"""Transaction models"""
from decimal import Decimal

from pydantic import BaseModel


class Transaction(BaseModel):
    """Transaction class"""

    sender: str
    recipient: str
    amount: Decimal
