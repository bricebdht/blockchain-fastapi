from datetime import datetime

from pytest import fixture

from app.models.block_model import Block
from app.models.node_model import Node


@fixture(scope="function", autouse=True)
def init_mongo():
    Block.get_collection().drop()
    Node.get_collection().drop()
    first_block = Block(index=0, timestamp=datetime.now(), transactions=[], proof=0)
    first_block.insert()
