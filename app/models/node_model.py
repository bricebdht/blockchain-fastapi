from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from app.database import client
from app.settings import settings

COLLECTION_NAME: str = "nodes"


class Node(BaseModel):
    index: Optional[int]
    address: str

    @classmethod
    def get_collection(cls):
        return client[settings.database_name][COLLECTION_NAME]

    @classmethod
    def get_last_node(cls) -> Dict[str, Any]:
        cursor = list(Node.get_collection().find().sort("index", -1).limit(1))
        current_node = cursor[0]
        return current_node

    def insert(self) -> None:
        client[settings.database_name][COLLECTION_NAME].insert_one(self.dict())
