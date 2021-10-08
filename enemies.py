import pygame
from support import get_frames
from random import randint, choice
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.frames = get_frames(choice(ENEMIES_PATH))
        self.frame_index = 0
        self.animation_speed = 0.2
        self.looking_left = False
        self.image = pygame.transform.flip(self.frames[int(self.frame_index)],self.looking_left, False)
        self.rect = self.image.get_rect(center = pos)
        self.set_speed()    
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = pygame.transform.flip(self.frames[int(self.frame_index)],self.looking_left, False)

    def set_speed(self):
        speed_x = 0
        speed_y = 0
        while speed_x == 0 and speed_y == 0:
            speed_x = randint(-SPEED + 1, SPEED - 1)
            speed_y = randint(-SPEED + 1, SPEED - 1)
        if speed_x < 0:
            self.looking_left = True
        elif speed_x > 0:
            self.looking_left = False
        self.speed = pygame.math.Vector2(speed_x, speed_y)
    
    def move(self, walls):
        self.update(self.speed)
        for wall in walls:
            if wall.rect.colliderect(self.rect):
                self.update(-self.speed)
                self.set_speed()
                break

    def update(self, speed):
        self.rect.center += speed
