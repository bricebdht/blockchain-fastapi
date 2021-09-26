from decimal import Decimal

from pydantic import BaseModel


class Transaction(BaseModel):
    sender: str
    recipient: str
    amount: Decimal
