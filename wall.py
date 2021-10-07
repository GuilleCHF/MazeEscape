import pygame
from settings import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2) -> None:
        super().__init__()
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1,y2)
        self.y2 = max(y1,y2)
        if self.is_horizontal() and self.is_vertical():
            raise Exception("Walls must be horizontal or vertical.")
        width = (self.x2 - self.x1) * TILE_SIZE + WALL_THICKNESS
        height = (self.y2 - self.y1) * TILE_SIZE + WALL_THICKNESS
        pos = (self.x1 * TILE_SIZE - WALL_THICKNESS//2, self.y1 * TILE_SIZE - WALL_THICKNESS//2)
        self.image = pygame.Surface((width, height))
        self.image.fill(WALL_COLOR)
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, speed: pygame.math.Vector2):
        self.rect.center += speed
    
    def is_vertical(self) -> bool:
        return self.x1 == self.x2
    def is_horizontal(self) -> bool:
        return self.y1 == self.y2
    
    def get_coords(self) -> tuple:
        return (self.x1, self.y1, self.x2, self.y2)
    
    def __repr__(self) -> str:
        return f"W@(x1,y1,x2,y2)={self.x1,self.y1,self.x2,self.y2})"