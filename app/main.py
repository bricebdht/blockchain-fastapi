"""
Main
"""
from fastapi import FastAPI

from app.routers import mine, transactions

app = FastAPI()
app.include_router(transactions.router)
app.include_router(mine.router)


@app.get("/")
def root():
    """Healthcheck API to make sure the app is responding"""
    return {"status": "OK"}
