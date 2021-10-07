import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill("blue")
        pos = (SCREEN_SIZE//2, SCREEN_SIZE//2)
        self.rect = self.image.get_rect(center = pos)
    
    def update(self, speed: pygame.math.Vector2) -> None:
        self.rect.center += speed