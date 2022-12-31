"""
APIs related to nodes
"""
from fastapi import APIRouter

from app.models.block_model import Block, Transaction
from app.models.node_model import Node

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
