'''
Stolen from previous project
'''
import random
from typing import List, Tuple
class Map:
    def __init__(
        self,
        size: int,
        extra_connection_chance: float = 0.05
    ):
        if size < 5:
            raise ValueError("Size must be at least 5 to create a map.")
        if not (0.0 <= extra_connection_chance <= 1.0):
            raise ValueError("Extra connection chance must be between 0 and 1.")
        if size % 2 == 0:
            size -= 1
        self.player = None
        self.size = size
        self.grid: List[List[int]] = [[0] * size for _ in range(size)]
        self.home = (size // 2, size // 2)
        self.grid[self.home[0]][self.home[1]] = 1
        self.room_chance = 0.4
        self.extra_connection_chance = extra_connection_chance
        self.generate()

    def generate(self) -> List[List[int]]:
        dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        stack: List[Tuple[int, int]] = [self.home]
        while stack:
            x, y = stack[-1]
            neighbors: List[Tuple[int, int]] = []
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if self._inBounds(nx, ny) and self.grid[nx][ny] == 0:
                    neighbors.append((nx, ny))
            if neighbors:
                nx, ny = random.choice(neighbors)
                wall_x, wall_y = (x + nx) // 2, (y + ny) // 2
                self.grid[wall_x][wall_y] = 2 
                self.grid[nx][ny] = 2         
                stack.append((nx, ny))
            else:
                stack.pop()
        dead_ends: List[Tuple[int, int]] = []
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 2:

                    count_adjacent_passages = 0
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + dx, j + dy
                        if self._inBounds(ni, nj) and self.grid[ni][nj] in (1, 2):
                            count_adjacent_passages += 1
                    if count_adjacent_passages == 1:
                        dead_ends.append((i, j))
        room = random.choice(dead_ends)
        self.grid[room[0]][room[1]] = 3  
        self._addExtraConnections()
        return self.grid

    def _addExtraConnections(self):
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if self.grid[i][j] != 0:
                    continue 
                north = self.grid[i - 1][j]
                south = self.grid[i + 1][j]
                if north in (1, 2, 3) and south in (1, 2, 3):
                    left = self.grid[i][j - 1]
                    right = self.grid[i][j + 1]
                    if left == 0 and right == 0 and random.random() < self.extra_connection_chance:
                        self.grid[i][j] = 2
                    continue
                west = self.grid[i][j - 1]
                east = self.grid[i][j + 1]
                if west in (1, 2, 3) and east in (1, 2, 3):
                    up = self.grid[i - 1][j]
                    down = self.grid[i + 1][j]
                    if up == 0 and down == 0 and random.random() < self.extra_connection_chance:
                        self.grid[i][j] = 2

    def _inBounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size

    def printMap(self):
        cell_repr = {
            0: '  ',
            1: 'H ',
            2: '. ',
            3: 'R ',
            4: '* '  # Placeholder for future use
        }
        print('┌' + '─' * (2 * self.size) + '┐')
        for row in self.grid:
            line = ''.join(cell_repr[cell] for cell in row)
            print(f'│{line}│')
        print('└' + '─' * (2 * self.size) + '┘')
        print(" H = Home")
        print(" . = Hallway")
        print(" R = Room")

    def markShortestPath(self, path: List[Tuple[int, int]]):
        path = path[1:-1]
        for x, y in path:
            if self._inBounds(x, y):
                self.grid[x][y] = 4

    def regenerate(self):
        self.grid: List[List[int]] = [[0] * self.size for _ in range(self.size)]
        self.home = (self.size // 2, self.size // 2)
        self.grid[self.home[0]][self.home[1]] = 1
        self.generate()
    