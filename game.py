import pygame
from maze import Maze
from player import Player
from settings import *

class Game():
    def __init__(self) -> None:
        self.maze = Maze(MAZE_SIZE)
        self.maze_surf = self.maze.draw()
        self.pos_x_map = (SCREEN_SIZE * MAZE_SCALE) // (MAZE_SIZE * 2)
        self.pos_y_map = self.pos_x_map
        self.pos_x_screen = SCREEN_SIZE//2
        self.pos_y_screen = self.pos_x_screen
        self.player = Player()
    
    def update_pos(self):
        key_pressed = pygame.key.get_pressed()
        up_pressed = key_pressed[pygame.K_UP]
        down_pressed = key_pressed[pygame.K_DOWN]
        left_pressed = key_pressed[pygame.K_LEFT]
        right_pressed = key_pressed[pygame.K_RIGHT]
        speed_x = 0
        speed_y = 0
        
        if up_pressed: speed_y -= SPEED
        if down_pressed: speed_y += SPEED
        if left_pressed: speed_x -= SPEED
        if right_pressed: speed_x += SPEED
        
        self.pos_x_map += speed_x
        self.pos_y_map += speed_y
        self.pos_x_screen += speed_x
        self.pos_y_screen += speed_y
        
        self.pos_x_screen = min(self.pos_x_screen, SCREEN_SIZE// 4 * 3)
        self.pos_x_screen = max(self.pos_x_screen, SCREEN_SIZE// 4)
        self.pos_y_screen = min(self.pos_y_screen, SCREEN_SIZE// 4 * 3)
        self.pos_y_screen = max(self.pos_y_screen, SCREEN_SIZE// 4)
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.fill(EXT_COLOR)
        screen.blit(self.maze_surf, (self.pos_x_screen-self.pos_x_map, self.pos_y_screen-self.pos_y_map))
        pygame.draw.circle(screen, "red", (self.pos_x_screen, self.pos_y_screen), PLAYER_SIZE // 2)
    