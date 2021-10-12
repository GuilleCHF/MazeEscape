import pygame
from pygame import draw
from pygame.constants import K_SPACE
from support import fill_whith_image
from pixelfont import PixelFont
from settings import *


class Title():
    def __init__(self, screen) -> None:
        self.screen = screen

        self.title_font = PixelFont(28, img_path = WALL_IMAGE)
        self.font_small = PixelFont(5, color = "grey40")
        self.font_big = PixelFont(15, img_path = WALL_IMAGE)

        # Main image
        self.image = pygame.Surface((SCREEN_SIZE,SCREEN_SIZE))
        fill_whith_image(self.image, pygame.image.load(FLOOR_IMAGE))
        
        maze_word = self.title_font.pixel_word("maze")
        self.image.blit(maze_word, maze_word.get_rect(midtop  = (SCREEN_SIZE//2, 50)))
        escape_word = self.title_font.pixel_word("escape")
        self.image.blit(escape_word, escape_word.get_rect(midtop  = (SCREEN_SIZE//2, 250)))

        # Game status
        self.win = False
        self.lose = False
    
    def draw(self):
        self.screen.fill("black")
        self.screen.blit(self.image, (0,0))
        message = self.font_small.pixel_word("Press Spacebar to start new Game")
        self.screen.blit(message, message.get_rect(midbottom = (SCREEN_SIZE//2, SCREEN_SIZE - 50)))
        if self.win:
            self.draw_win_lose("win")
        elif self.lose:
            self.draw_win_lose("lose")

    def draw_win_lose(self, res):
        msg = self.font_big.pixel_word(f"You {res}!")
        self.screen.blit(msg, msg.get_rect(center = (SCREEN_SIZE//2, SCREEN_SIZE * 3 //4)))


    def run(self):
        self.draw()
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            return "new game"
        else:
            return "title"