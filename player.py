import pygame
from settings import *


class Player():
    def __init__(self) -> None:
        self.pos_x_map = (SCREEN_SIZE * MAZE_SCALE) // (MAZE_SIZE * 2)
        self.pos_y_map = self.pos_x_map
        self.pos_x_screen = SCREEN_SIZE//2
        self.pos_y_screen = self.pos_x_screen
    
    def move_player(self) -> None:
        pass