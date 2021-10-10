import pygame
from settings import *
from game import Game
from title import Title

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Maze Escape")
    clock = pygame.time.Clock()
    
    my_game = None
    my_title = Title(screen)
    game_status = "title"
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if game_status == "run":
            game_status = my_game.run()
        elif game_status == "title":
            game_status = my_title.run()
        elif game_status == "new game":
            my_game = Game(screen)
            game_status = "run"
        
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    pass


if __name__ == "__main__":
    main()