"""
APIs related to blocks
"""
from datetime import datetime
from hashlib import sha256

from fastapi import APIRouter

from app.models.block_model import Block
from app.settings import NODE_IDENTIFIER

router = APIRouter(
    prefix="/mine",
    tags=["Mine"],
)


def validate_proof(last_proof: int, proof: int) -> bool:
    guess = f"{last_proof}{proof}".encode()
    guess_hash = sha256(guess).hexdigest()
    return guess_hash[:4] == "aaaa"


@router.get("/")
def get() -> Block:
    """Mining a new block"""
    last_block = Block.get_last_block()
    last_proof = last_block["proof"]
    proof: int = 0
    while validate_proof(last_proof=last_proof, proof=proof) is False:
        proof += 1

    new_block = Block(
        index=last_block["index"] + 1,
        timestamp=datetime.now(),
        transactions=[
            {"sender": "0", "recipient": NODE_IDENTIFIER, "amount": 1}
        ],  # First transaction to reward the miner
        proof=proof,
    )
    new_block.insert()

    return new_block
