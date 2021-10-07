import pygame
from settings import *
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Maze Escape")
    clock = pygame.time.Clock()
    
    my_game = Game(screen)
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        my_game.run()
        
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    pass


if __name__ == "__main__":
    main()