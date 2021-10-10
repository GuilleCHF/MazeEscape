from pathlib import Path

SCREEN_SIZE = 700
MAZE_SIZE = 10
TILE_SIZE = 384
WALL_THICKNESS = 64
SPEED = 3
ENEMY_RATE = 100

# MAZE_SCALE = 4
# TILE_SIZE = (SCREEN_SIZE * MAZE_SCALE) // MAZE_SIZE
# WALL_THICKNESS = TILE_SIZE // 5
# WALL_COLOR = "grey50"
# CELL_COLOR = "goldenrod"
# EXT_COLOR = "darkgreen"

ENEMIES_PATH = [Path(r"./images/enemies/1"), Path(r"./images/enemies/2")] 
WALL_IMAGE = Path(r"./images/maze/wall4.png")
FLOOR_IMAGE = Path(r"./images/maze/floor4.png")
OUTSIDE_IMAGE = Path(r"./images/maze/outside2.png")
