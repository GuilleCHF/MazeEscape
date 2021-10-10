import pygame
from settings import *


class Title():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.image = pygame.Surface((100,100))
        self.image.fill("orange")
        pos = (SCREEN_SIZE//2, SCREEN_SIZE//3)
        self.rect = self.image.get_rect(center = pos)
    
    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.image, self.rect)
    
    def run(self):
        self.draw()
        keys = pygame.key.get_pressed()
        return keys[pygame.K_RETURN]