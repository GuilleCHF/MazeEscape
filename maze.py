import random
import pygame
import time
from settings import *
from random import choice


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

class Wall():
    _instances= {}
    def __new__(cls, x1, y1, x2, y2):
        xx_1 = min(x1, x2)
        xx_2 = max(x1, x2)
        yy_1 = min(y1, y2)
        yy_2 = max(y1, y2)
        key = (xx_1, yy_1, xx_2, yy_2)
        if (obj := cls._instances.get(key)) is not None:
            return obj
        new = super().__new__(cls)
        cls._instances[key] = new
        new.__init(xx_1, yy_1, xx_2, yy_2)
        return new
    
    # def __init__(self) -> None:
    #     5
    #     pass

    def __init(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.is_horizontal() and self.is_vertical():
            raise Exception("Walls must be horizontal or vertical.")
    
    def is_vertical(self) ->bool:
        return self.x1 == self.x2
    def is_horizontal(self) -> bool:
        return self.y1 == self.y2
    
    def __repr__(self) -> str:
        return f"W@(x1,y1,x2,y2)={self.x1,self.y1,self.x2,self.y2})"
    def __eq__(self, o: object) -> bool:
        return (self.x1 == o.x1) and (self.x2 == o.x2) and (self.y1 == o.y1) and (self.y2 == o.y2)

def get_wall(cell_1: Cell, cell_2: Cell) -> Wall:
    x1 = min(cell_1.j, cell_2.j)
    x2 = max(cell_1.j, cell_2.j)
    y1 = min(cell_1.i, cell_2.i)
    y2 = max(cell_1.i, cell_2.i)
    test_list = [abs(x1-x2), abs(y1-y2)]
    test_list.sort()
    if test_list != [0, 1]:
        raise Exception("Cells mus be adjacents to create a wall in between")
    return Wall(x1+1, y1+1, x2, y2)

class Maze():
    def __init__(self, maze_size) -> None:
        random.seed(1)
        self.maze_size = maze_size
        self.map = [[Cell(i,j) for j in range(self.maze_size)] for i in range(self.maze_size)]
        self.walls: list[Wall]
        self.walls = []
        self.walls.append(Wall(0, 0, self.maze_size, 0))
        self.walls.append(Wall(0, 0, 0, self.maze_size))
        self.walls.append(Wall(self.maze_size, self.maze_size, self.maze_size, 0))
        self.walls.append(Wall(self.maze_size, self.maze_size, 0, self.maze_size))
        
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if j + 1 < self.maze_size:
                    self.walls.append(get_wall(self.map[i][j],self.map[i][j+1]))
                if i + 1 < self.maze_size:
                    self.walls.append(get_wall(self.map[i][j],self.map[i+1][j]))
        self.conn = []
        self.initialize()
        pass
    
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
        # new_conn = Conn(origin, destiny)
        new_conn = (origin, destiny)
        origin.add_conn(destiny)
        destiny.add_conn(origin)
        self.conn.append(new_conn)
        wall = get_wall(origin, destiny)
        self.walls.remove(wall)
    
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
    
    def draw(self) -> pygame.Surface:
        my_surf = pygame.Surface((SCREEN_SIZE * MAZE_SCALE, SCREEN_SIZE * MAZE_SCALE))
        my_surf.fill(CELL_COLOR)
        for wall in self.walls:
            x1 = wall.x1 * TILE_SIZE - PADDING
            y1 = wall.y1 * TILE_SIZE - PADDING
            x2 = wall.x2 * TILE_SIZE + PADDING
            y2 = wall.y2 * TILE_SIZE + PADDING
            width = x2 - x1
            height = y2 - y1
            new_surf = pygame.Surface((width, height))
            new_surf.fill(WALL_COLOR)
            my_surf.blit(new_surf,(x1, y1))
        return my_surf




