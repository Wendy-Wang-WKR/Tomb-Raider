from src.core.map import TileKind

tile_kinds = [
    TileKind("dirt", "土.png", False), # 0
    TileKind("grass", "草.png", False), # 1
    TileKind("road2", "路拐.png", False, rotate = 270), # 2
    TileKind("road3", "路.png", False, rotate = 90), # 3
    TileKind("road4", "路.png", False, rotate = 270), # 4
    TileKind("road5", "路.png", False, rotate = 0), # 5
    TileKind("road6", "路.png", False, rotate = 180), # 6
    TileKind("road7", "路拐.png", False, rotate = 0), # 7
    TileKind("road8", "路拐.png", False, rotate = 90), # 8
    TileKind("road9", "路拐.png", False, rotate = 180), # 9
]