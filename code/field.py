import pygame
from pygame import image
from settings import *


class Field(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE*MAZE_SIZE,TILE_SIZE*MAZE_SIZE))
        self.image.fill(CELL_COLOR)
        self.rect = self.image.get_rect(topleft=(0,0))
    
    def update(self, speed: pygame.math.Vector2):
        self.rect.center += speed