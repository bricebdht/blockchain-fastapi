from fastapi import APIRouter

router = APIRouter()


@router.post("/transactions/new", methods=["POST"])
def post() -> None:
    return "Add transaction"
