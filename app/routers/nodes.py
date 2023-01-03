"""
APIs related to nodes
"""
from typing import List

import requests
from fastapi import APIRouter

from app.models.block_model import Block
from app.models.node_model import Node
from app.routers.mine import validate_proof

router = APIRouter(
    prefix="/nodes",
    tags=["Nodes"],
)


@router.post("/register")
def post(node_data: Node) -> str:
    """Create a new node in database"""
    try:
        last_node = Node.get_last_node()
        new_index = last_node["index"] + 1
    except IndexError as err:
        new_index = 0
    new_node = Node(index=new_index, address=node_data.address)
    new_node.insert()
    return "Node has been registered"


def validate_chain(chain: List[Block]):
    last_block = Block.get_last_block()
    for i in range(1, len(chain)):
        block = chain[i]
        if block["previous_hash"] != Block(**last_block).hash():
            return False
        if not validate_proof(last_proof=last_block["proof"], proof=block["proof"]):
            return False
        last_block = block
    return True


@router.get("/resolve")
def get() -> str:
    """
    Resolve conflicts with the chains of other nodes
    The longest chain is considered the right one
    """
    # Get chains from other nodes
    nodes = Node.get_collection().find()
    current_length = Block.get_collection().count_documents({})
    for node in nodes:
        response = requests.get(f"{node['address']}/chain")
        chain = response.json()
        length = len(chain)
        if length > current_length and validate_chain(chain=chain):
            for i in range(current_length, length):
                new_block = Block(**chain[i])
                new_block.insert()
            return "The blockain has been updated"

    return "The blockchain is already up to date"
