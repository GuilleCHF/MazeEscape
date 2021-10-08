import pygame
from pygame import image
from support import fill_whith_image
from settings import *


class Field(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        size = TILE_SIZE * MAZE_SIZE + 2 * SCREEN_SIZE
        outside = pygame.Surface((size,size))
        image = pygame.image.load(OUTSIDE_IMAGE)
        fill_whith_image(outside, image)

        size = TILE_SIZE * MAZE_SIZE
        maze = pygame.Surface((size,size))
        image = pygame.image.load(FLOOR_IMAGE)
        fill_whith_image(maze, image)

        self.image = outside
        self.image.blit(maze,(SCREEN_SIZE,SCREEN_SIZE))
        self.rect = self.image.get_rect(topleft=(-SCREEN_SIZE,-SCREEN_SIZE))
    
    def update(self, speed: pygame.math.Vector2):
        self.rect.center += speed