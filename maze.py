import pygame
import sys
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
        return f"cell@[{self.i},{self.j}]"

class Maze():
    def __init__(self, maze_size) -> None:
        self.maze_size = maze_size
        self.map = [[Cell(i,j) for j in range(self.maze_size)] for i in range(self.maze_size)]
        self.conn = []
        self.initialize()
    
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





