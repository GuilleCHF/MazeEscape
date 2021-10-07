import pygame
from settings import *


class Goal(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        size = TILE_SIZE - WALL_THICKNESS - 2*PLAYER_SIZE
        pos = TILE_SIZE * (MAZE_SIZE-1) + WALL_THICKNESS//2 + PLAYER_SIZE
        self.image = pygame.Surface((size, size))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(topleft = (pos, pos))
    
    def update(self, speed: pygame.math.Vector2):
        self.rect.center += speed