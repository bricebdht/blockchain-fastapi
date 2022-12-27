"""Transaction models"""

from pydantic import BaseModel

from app.database import client
from app.settings import settings

COLLECTION_NAME: str = "transactions"


class Transaction(BaseModel):
    """Transaction class"""

    sender: str
    recipient: str
    amount: float  # Need to update to use Decimal type

    def insert(self) -> None:
        client[settings.database_name][COLLECTION_NAME].insert_one(self.dict())

    @classmethod
    def get_collection(cls):
        return client[settings.database_name][COLLECTION_NAME]
