from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel

from app.database import client
from app.settings import settings

COLLECTION_NAME: str = "blocks"


class Transaction(BaseModel):
    """Transaction class"""

    sender: str
    recipient: str
    amount: float  # Need to update to use Decimal type


class Block(BaseModel):
    """Block class"""

    index: int
    timestamp: datetime
    transactions: List[Transaction]
    proof: int = None
    previous_hash: str = None

    @classmethod
    def get_collection(cls):
        return client[settings.database_name][COLLECTION_NAME]

    def insert(self) -> None:
        client[settings.database_name][COLLECTION_NAME].insert_one(self.dict())

    def update(self, updated_fields: Dict[str, Any]) -> None:
        client[settings.database_name][COLLECTION_NAME].update_one(
            {"index": self.index}, {"$set": updated_fields}
        )
