from os import path
import pygame
from settings import *
from support import get_frames


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.walk_frames = get_frames(path.join("images","player","walk"))
        self.stand_frames = get_frames(path.join("images","player","stand"))
        self.frames = self.stand_frames
        self.frame_index = 0
        self.animation_speed = 0.2
        self.to_right = True
        self.image = pygame.transform.flip(self.frames[int(self.frame_index)],self.to_right, False)
        pos = (SCREEN_SIZE//2, SCREEN_SIZE//2)
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self, speed: pygame.math.Vector2 = pygame.math.Vector2(0,0)):
        if speed.x == 0 and speed.y == 0:
            self.frames = self.stand_frames
        else:
            self.frames = self.walk_frames
        
        if speed.x > 0:
            self.to_right = True
        elif speed.x < 0:
            self.to_right = False

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        
        self.image = pygame.transform.flip(self.frames[int(self.frame_index)],self.to_right, False) 

    def update(self, speed: pygame.math.Vector2) -> None:
        self.rect.center += speed