import pygame
from maze import Maze
from settings import *


def main():
    my_maze = Maze(20)
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Maze Escape")
    my_maze.draw(screen)
    pygame.display.update()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
    pass


if __name__ == "__main__":
    main()