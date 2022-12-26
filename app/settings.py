from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str = "blockchain"


settings = Settings()
