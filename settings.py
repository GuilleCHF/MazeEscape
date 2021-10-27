from os import path
from enum import Enum, auto

SCREEN_SIZE = 700
MAZE_SIZE = 10
TILE_SIZE = 384
WALL_THICKNESS = 64
SPEED = 3
ENEMY_RATE = 100

ENEMIES_PATH = [path.join("images","enemies","1"), path.join("images","enemies","2")] 
WALL_IMAGE = path.join("images","maze","wall5.png")
FLOOR_IMAGE = path.join("images","maze","floor5.png")
OUTSIDE_IMAGE = path.join("images","maze","outside3.png")


class GameStatus(Enum):
    TITLE = auto()
    RUN = auto()
    WIN = auto()
    LOSE = auto()
    NEW_GAME = auto()