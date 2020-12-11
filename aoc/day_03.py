from collections import deque
from functools import reduce
from math import ceil
from typing import Any, List


class Tile:
    def __init__(self, x: int, y: int, data: Any = None):
        self.x = x
        self.y = y
        self.data = data

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.x == other.x and self.y == other.y
        else:
            return self.data == other

    def __iter__(self):
        return iter([self.x, self.y])

    def __hash__(self):
        return hash(tuple(self))

    def __str__(self):
        return f"Tile({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()


class Grid:
    def __init__(self, grid: List[str], offset: Tile):
        # TODO: must replace, very memory ineficient way to find the optimal width of our grid
        columns = ceil(len(grid[0]) / offset.x) * ceil(len(grid) / offset.y) + 1
        self.grid = [list(row) * columns for row in grid]
        self.offset = offset
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def move(self, origin: Tile) -> Tile:
        (x, y) = list(tuple(u + v for u, v in zip(origin, self.offset)))
        if self.width > x >= 0 and self.height > y >= 0:
            yield Tile(x, y, self.grid[y][x])


class Graph:
    def __init__(self, grid: List[str], start: Tile):
        self.grid = grid
        self.start = start

    def walk(self, offset: Tile) -> List[Tile]:
        grid = Grid(self.grid, offset)
        queue = deque([])
        queue.append(self.start)
        tiles = []
        while queue:
            current = queue.popleft()
            for nearest in grid.move(current):
                queue.append(nearest)
                tiles.append(nearest)
        return tiles


def calculate_total(tiles: List[Tile]) -> int:
    return sum([1 for tile in tiles if tile == "#"])


def answer1(input: List[str]) -> int:
    graph = Graph(input, Tile(0, 0))
    return calculate_total(graph.walk(Tile(3, 1)))


def answer2(input: List[str]) -> int:
    graph = Graph(input, Tile(0, 0))
    offsets = [Tile(3, 1), Tile(1, 1), Tile(5, 1), Tile(7, 1), Tile(1, 2)]
    scenarios = (calculate_total(graph.walk(offset)) for offset in offsets)
    return reduce((lambda x, y: x * y), scenarios)
