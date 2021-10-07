import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill("blue")
        pos = (SCREEN_SIZE//2, SCREEN_SIZE//2)
        self.rect = self.image.get_rect(center = pos)
        # self.pos_x_map = (SCREEN_SIZE * MAZE_SCALE) // (MAZE_SIZE * 2)
        # self.pos_y_map = self.pos_x_map
        # self.pos_x_screen = SCREEN_SIZE//2
        # self.pos_y_screen = self.pos_x_screen
    
    def update(self, speed: pygame.math.Vector2) -> None:
        self.rect.center += speed