import pygame
from pygame import sprite
from maze import Maze
from player import Player
from goal import Goal
from field import Field
from settings import *

class Game():
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        # Maze
        self.maze = Maze(MAZE_SIZE)
        
        self.walls = self.maze.walls_group()
        self.goal = pygame.sprite.GroupSingle()
        self.goal.add(Goal())
        self.field =pygame.sprite.GroupSingle()
        self.field.add(Field())
        
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.speed = pygame.math.Vector2(0,0)
        
        pos = (SCREEN_SIZE - TILE_SIZE) // 2
        self.world_update(pygame.math.Vector2(pos, pos))
    
    def run(self):
        self.get_input()
        self.update()
        self.draw()
        
    
    def get_input(self):
        key_pressed = pygame.key.get_pressed()
        up_pressed = key_pressed[pygame.K_UP]
        down_pressed = key_pressed[pygame.K_DOWN]
        left_pressed = key_pressed[pygame.K_LEFT]
        right_pressed = key_pressed[pygame.K_RIGHT]
        self.speed.x = 0
        self.speed.y = 0
        
        if up_pressed:
            self.speed.y -= SPEED
        if down_pressed:
            self.speed.y += SPEED
        if left_pressed:
            self.speed.x -= SPEED
        if right_pressed:
            self.speed.x += SPEED
    
    def update(self):
        player = self.player.sprite
        speed_x = self.speed.x
        speed_y = self.speed.y

        # x movement and collision
        player.update(pygame.math.Vector2(speed_x,0))
        for wall in self.walls:
            if wall.rect.colliderect(player.rect):
                if speed_x > 0:
                    D_x = wall.rect.left - player.rect.right
                else:
                    D_x = wall.rect.right - player.rect.left
                player.update(pygame.math.Vector2(D_x,0))
        
        # y movement and collision
        player.update(pygame.math.Vector2(0,speed_y))
        for wall in self.walls:
            if wall.rect.colliderect(player.rect):
                if speed_y > 0:
                    D_y = wall.rect.top - player.rect.bottom
                else:
                    D_y = wall.rect.bottom - player.rect.top
                player.update(pygame.math.Vector2(0,D_y))
        
        # world shift
        if player.rect.centerx > int(SCREEN_SIZE * 3 / 4):
            world_shift_x = int(SCREEN_SIZE * 3 / 4) - player.rect.centerx
        elif player.rect.centerx < int(SCREEN_SIZE / 4):
            world_shift_x = int(SCREEN_SIZE / 4) - player.rect.centerx
        else:
            world_shift_x = 0
        
        if player.rect.centery > int(SCREEN_SIZE * 3 / 4):
            world_shift_y = int(SCREEN_SIZE * 3 / 4) - player.rect.centery
        elif player.rect.centery < int(SCREEN_SIZE / 4):
            world_shift_y = int(SCREEN_SIZE / 4) - player.rect.centery
        else:
            world_shift_y = 0
        
        world_shift = pygame.math.Vector2(world_shift_x, world_shift_y)
        player.update(world_shift)
        self.world_update(world_shift)
    
    def world_update(self, world_shift):
        self.field.update(world_shift)
        self.walls.update(world_shift)
        self.goal.update(world_shift)
    
    def draw(self) -> None:
        self.screen.fill(EXT_COLOR)

        self.field.draw(self.screen)        
        self.walls.draw(self.screen)
        self.goal.draw(self.screen)

        self.player.draw(self.screen)
    