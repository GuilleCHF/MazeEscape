import pygame
from maze import Maze
from settings import *


def main():
    my_maze = Maze(MAZE_SIZE)
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Maze Escape")
    clock = pygame.time.Clock()
    
    maze_surf = my_maze.draw()
    # maze_surf_big = pygame.transform.rotozoom(maze_surf,0,2)
    
    # test_timer = pygame.USEREVENT+1
    # pygame.time.set_timer(test_timer, 50)
    
    # maze_surf_big = pygame.transform.scale2x(maze_surf)
    # maze_surf_big = pygame.transform.scale2x(maze_surf_big)
    pos_x_map = (SCREEN_SIZE * MAZE_SCALE) // (MAZE_SIZE * 2)
    pos_y_map = pos_x_map
    pos_x = SCREEN_SIZE//2
    pos_y = pos_x
    speed = 2
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        up_pressed = key_pressed[pygame.K_UP]
        down_pressed = key_pressed[pygame.K_DOWN]
        left_pressed = key_pressed[pygame.K_LEFT]
        right_pressed = key_pressed[pygame.K_RIGHT]
        speed_x = 0
        speed_y = 0
        
        if up_pressed: speed_y -= speed
        if down_pressed: speed_y += speed
        if left_pressed: speed_x -= speed
        if right_pressed: speed_x += speed
        pos_x_map += speed_x
        pos_y_map += speed_y
        pos_x += speed_x
        pos_y += speed_y
        pos_x = min(pos_x, SCREEN_SIZE// 4 * 3)
        pos_x = max(pos_x, SCREEN_SIZE// 4)
        pos_y = min(pos_y, SCREEN_SIZE// 4 * 3)
        pos_y = max(pos_y, SCREEN_SIZE// 4)
        
        screen.fill("black")
        screen.blit(maze_surf, (pos_x-pos_x_map, pos_y-pos_y_map))
        pygame.draw.circle(screen, "red", (pos_x, pos_y), 5)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    pass


if __name__ == "__main__":
    main()