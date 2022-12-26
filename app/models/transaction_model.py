"""Transaction models"""

from pydantic import BaseModel

from app.database import client
from app.settings import settings

COLLECTION_NAME = "transactions"


class Transaction(BaseModel):
    """Transaction class"""

    sender: str
    recipient: str
    amount: float  # Need to update to use Decimal type

    def insert(self) -> None:
        client[settings.database_name][COLLECTION_NAME].insert_one(self.dict())

    @classmethod
    def get(cls, *args, **kwargs):
        return client[settings.database_name][COLLECTION_NAME].find(kwargs)

    @classmethod
    def count(cls, *args, **kwargs):
        return client[settings.database_name][COLLECTION_NAME].count_documents(kwargs)

    @classmethod
    def collection(cls):
        return client[settings.database_name][COLLECTION_NAME]
