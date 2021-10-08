import pygame
from support import get_frames
from settings import *


class Goal(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.frames = get_frames("images\\goal")
        self.frame_index = 0
        self.animation_speed = .15
        pos = TILE_SIZE * MAZE_SIZE - TILE_SIZE // 2 
        self.image = self.frames[int(self.frame_index)]
        self.rect = self.image.get_rect(center = (pos, pos))
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
    
    def update(self, speed: pygame.math.Vector2):
        self.rect.center += speed