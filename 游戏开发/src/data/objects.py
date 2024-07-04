from src.components.entity import Entity
from src.components.sprite import Sprite
from src.components.player import Player
from src.components.physics import Body
from src.core.config import TILESIZE

entity_factories = [
    # 0 makes a player
    lambda args: Entity(Player(), Sprite("lara.png"), Body(30, 80, 30, 8)),

    # 1 makes a tree
    lambda args: Entity(Sprite("tree.png"), Body(32, 80, 24, 8)),

    # 2 makes a tree
    lambda args: Entity(Sprite("manor.png"), Body(90,30,1020,330))
]

def create_entity(id, x, y, data=None):
    factory = entity_factories[id]
    e =  factory(data)
    e.x = x*TILESIZE
    e.y = y*TILESIZE
    return e