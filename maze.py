import random
import pygame
from settings import *
from random import choice
from wall import Wall


class Conn():
    def __init__(self, el1, el2) -> None:
        self.el1 = el1
        self.el2 = el2
    
    def get_els(self) -> list:
        return [self.el1, self.el2]


class Cell():
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j
        self.visited = False
        self.conn = []
    
    def add_conn(self, conn):
        self.conn.append(conn)
    
    def __repr__(self) -> str:
        return f"C@[{self.i},{self.j}]"


def get_wall(cell_1: Cell, cell_2: Cell, coords_only = False) -> Wall:
    x1 = min(cell_1.j, cell_2.j)
    x2 = max(cell_1.j, cell_2.j)
    y1 = min(cell_1.i, cell_2.i)
    y2 = max(cell_1.i, cell_2.i)
    test_list = [abs(x1-x2), abs(y1-y2)]
    test_list.sort()
    if test_list != [0, 1]:
        raise Exception("Cells mus be adjacents to create a wall in between")
    xx1 = min(x1 + 1, x2)
    xx2 = max(x1 + 1, x2)
    yy1 = min(y1 + 1, y2)
    yy2 = max(y1 + 1, y2)
    
    if coords_only:
        return (xx1, yy1, xx2, yy2)
    else:
        return Wall(xx1, yy1, xx2, yy2)


class Maze():
    def __init__(self, maze_size) -> None:
        random.seed(1)
        self.maze_size = maze_size
        
        # Cells
        self.map = [[Cell(i,j) for j in range(self.maze_size)] for i in range(self.maze_size)]
        
        # Walls
        self.walls_dict: dict[tuple, Wall] = {}
        my_wall = Wall(0, 0, self.maze_size, 0)
        self.walls_dict [my_wall.get_coords()] = my_wall
        my_wall = Wall(0, 0, 0, self.maze_size)
        self.walls_dict [my_wall.get_coords()] = my_wall
        my_wall = Wall(self.maze_size, self.maze_size, self.maze_size, 0)
        self.walls_dict [my_wall.get_coords()] = my_wall
        my_wall = Wall(self.maze_size, self.maze_size, 0, self.maze_size)
        self.walls_dict [my_wall.get_coords()] = my_wall
        
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if j + 1 < self.maze_size:
                    my_wall = get_wall(self.map[i][j],self.map[i][j+1])
                    self.walls_dict [my_wall.get_coords()] = my_wall
                if i + 1 < self.maze_size:
                    my_wall = get_wall(self.map[i][j],self.map[i+1][j])
                    self.walls_dict [my_wall.get_coords()] = my_wall
        
        # Initialize Maze
        self.conn = []
        self.initialize()
        self.walls = pygame.sprite.Group()
        for wall in self.walls_dict.values():
            self.walls.add(wall)
    
    def get_neighbours(self, curr: Cell) -> list[Cell]:
        curr_x = curr.i
        curr_y = curr.j
        res = []
        for i in range(-1,2):
            for j in range(-1,2):
                if (0 <= curr_x + i < self.maze_size) and (0 <= curr_y + j < self.maze_size):
                    if (i != 0) or (j != 0):
                        res.append(self.map[curr_x + i][curr_y + j])
        return res
    
    def get_neighbours_unvisited(self, curr: Cell) -> list[Cell]:
        neighbours = self.get_neighbours(curr)
        return [cell for cell in neighbours if not cell.visited]
    
    def get_rand_neighbour_unvisited(self, curr: Cell) -> Cell:
        unvisited = self.get_neighbours_unvisited(curr)
        if unvisited:
            return choice(unvisited)
        return None
    
    def get_adjacents(self, curr: Cell) -> list[Cell]:
        res = []
        i = curr.i
        j = curr.j
        
        if i > 0:
            res.append(self.map[i-1][j])
        if i < self.maze_size-1:
            res.append(self.map[i+1][j])
        if j > 0:
            res.append(self.map[i][j-1])
        if j < self.maze_size-1:
            res.append(self.map[i][j+1])
        
        return res
    
    def get_adjacents_unvisited(self, curr: Cell) -> list[Cell]:
        adj = self.get_adjacents(curr)
        return [cell for cell in adj if not cell.visited]
    
    def get_rand_adjacent_unvisited(self, curr: Cell) -> Cell:
        unvisited = self.get_adjacents_unvisited(curr)
        if unvisited:
            return choice(unvisited)
        return None
    
    def carve(self, origin: Cell, destiny: Cell) -> None:
        new_conn = (origin, destiny)
        origin.add_conn(destiny)
        destiny.add_conn(origin)
        self.conn.append(new_conn)
        wall_coords = get_wall(origin, destiny, True)
        del self.walls_dict[wall_coords]
    
    def initialize(self) -> None:
        self.map[0][0].visited = True
        stack = [self.map[0][0]]
        
        while stack:
            curr = stack.pop()
            new = self.get_rand_adjacent_unvisited(curr)
            if new:
                new.visited = True
                self.carve(curr, new)
                stack.append(curr)
                stack.append(new)
    
    def walls_group(self) -> pygame.sprite.Group:
        res = pygame.sprite.Group()
        for wall in self.walls:
            res.add(wall)
        return res
    
    # def set_end(self):
    #     size = TILE_SIZE - WALL_THICKNESS - 2*PLAYER_SIZE
    #     pos = TILE_SIZE * (MAZE_SIZE-1) + WALL_THICKNESS//2 + PLAYER_SIZE
    #     # self.end = pygame.Rect(pos, pos, size, size)
    #     self.end = pygame.sprite.Sprite()
    #     self.end.image = pygame.Surface((size, size))
    #     self.end.image.fill("yellow")
    #     self.end.rect = self.end.image.get_rect(topleft = (pos, pos))
    
    # def draw(self, screen):
    #     self.walls.draw(screen)
    #     screen.blit(self.end.image, self.end.rect)
    #     self.end.draw(screen)
    
    # def update(self, speed: pygame.math.Vector2) -> None:
    #     self.walls.update(speed)
    #     self.end.rect.center += speed
    
    # def _draw_cells(self) -> pygame.Surface:
    #     tile_size = (SCREEN_SIZE * MAZE_SCALE) // self.maze_size
    #     padding = tile_size // 10
    #     my_surf = pygame.Surface((SCREEN_SIZE * MAZE_SCALE, SCREEN_SIZE * MAZE_SCALE))
    #     my_surf.fill(WALL_COLOR)
    #     for conn in self.conn:
    #         i0 = conn[0].i
    #         j0 = conn[0].j
    #         i1 = conn[1].i
    #         j1 = conn[1].j
    #         left = min(j0, j1) * tile_size + padding
    #         top = min(i0, i1) * tile_size + padding
    #         width = (abs(j0 - j1) + 1) * tile_size - 2 * padding
    #         height = (abs(i0 - i1) + 1) * tile_size - 2 * padding
    #         new_surf = pygame.Surface((width, height))
    #         new_surf.fill(CELL_COLOR)
    #         my_surf.blit(new_surf,(left, top))
    #     return my_surf
    
    # def draw(self) -> pygame.Surface:
    #     my_surf = pygame.Surface((SCREEN_SIZE * MAZE_SCALE, SCREEN_SIZE * MAZE_SCALE))
    #     my_surf.fill(CELL_COLOR)
    #     for wall in self.walls_dict.values():
    #         x1 = wall.x1 * TILE_SIZE - PADDING
    #         y1 = wall.y1 * TILE_SIZE - PADDING
    #         x2 = wall.x2 * TILE_SIZE + PADDING
    #         y2 = wall.y2 * TILE_SIZE + PADDING
    #         width = x2 - x1
    #         height = y2 - y1
    #         new_surf = pygame.Surface((width, height))
    #         new_surf.fill(WALL_COLOR)
    #         my_surf.blit(new_surf,(x1, y1))
    #     return my_surf
    
    # def draw_walls(self, screen):
    #     self.walls.draw(screen)




