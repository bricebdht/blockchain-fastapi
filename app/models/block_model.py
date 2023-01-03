from datetime import datetime
from hashlib import sha256
from json import dumps, loads
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
    proof: int
    previous_hash: str = None

    @classmethod
    def get_collection(cls):
        return client[settings.database_name][COLLECTION_NAME]

    @classmethod
    def get_last_block(cls) -> Dict[str, Any]:
        cursor = list(Block.get_collection().find().sort("index", -1).limit(1))
        current_block = cursor[0]
        return current_block

    def insert(self) -> None:
        client[settings.database_name][COLLECTION_NAME].insert_one(self.dict())

    def update(self, updated_fields: Dict[str, Any]) -> None:
        client[settings.database_name][COLLECTION_NAME].update_one(
            {"index": self.index}, {"$set": updated_fields}
        )

    def hash(self) -> str:
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        stringified_block = dumps(loads(self.json()), sort_keys=True).encode()
        return sha256(stringified_block).hexdigest()
