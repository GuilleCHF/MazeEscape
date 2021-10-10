import pygame
from support import fill_whith_image
from settings import *


class Title():
    def __init__(self, screen) -> None:
        self.screen = screen
        bg = pygame.Surface((SCREEN_SIZE,SCREEN_SIZE))
        fill_whith_image(bg,pygame.image.load(OUTSIDE_IMAGE))
        title = pygame.image.load("images\\title\\title.png")
        title_rect = title.get_rect(center = (SCREEN_SIZE//2, SCREEN_SIZE//4))
        title_bg = pygame.Surface(title_rect.size)
        fill_whith_image(title_bg, pygame.image.load(FLOOR_IMAGE))
        self.image = bg
        self.image.blit(bg, (0,0))
        self.image.blit(title_bg, title_rect)
        self.image.blit(title, title_rect)

    
    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.image, (0,0))
    
    def run(self):
        self.draw()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return "new game"
        else:
            return "title"