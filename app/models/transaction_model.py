"""Transaction models"""

from pydantic import BaseModel


class Transaction(BaseModel):
    """Transaction class"""

    sender: str
    recipient: str
    amount: float  # Need to update to use Decimal type
