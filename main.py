import pygame
from settings import *
from game import Game
from title import Title

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Maze Escape")
    clock = pygame.time.Clock()
    
    my_game = Game(screen)
    my_title = Title(screen)
    game_running = False
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if game_running:
            game_running = my_game.run()
        else:
            game_running = my_title.run()
        
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    pass


if __name__ == "__main__":
    main()