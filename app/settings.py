from uuid import uuid4

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str = "blockchain"


settings = Settings()
NODE_IDENTIFIER = str(uuid4())
