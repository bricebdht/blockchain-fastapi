"""
Main
"""
from fastapi import FastAPI

from app.routers import transactions

app = FastAPI()
app.include_router(transactions.router)


@app.get("/")
def root():
    """Healthcheck API to make sure the app is responding"""
    return {"status": "OK"}
