from collections import deque
from math import ceil


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return iter([self.x, self.y])

    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, node):
        return self.x == node.x and self.y == node.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()


class Graph:
    TYPE_OPEN = "."
    TYPE_TREE = "#"

    def __init__(self, grid, offset):
        self.grid = self.expand_grid(grid, offset)
        self.offset = offset
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.values = {}

    def expand_grid(self, grid, offset):
        # this part feels dirty, I need to find an optimal algorithm to grow the grid
        factor = ceil(len(grid) / offset.y) + 1
        return [list(row) * factor for row in grid]

    def value_of(self, node):
        return self.grid[node.y][node.x]

    def is_tree(self, node):
        return self.value_of(node) == self.TYPE_TREE

    def walk(self, node):
        # use a bit of matrix arithmetic to move our cursor
        x, y = list(tuple(u + v for u, v in zip((node.x, node.y), self.offset)))
        # try not to overflow our grid
        if self.width > x >= 0 and self.height > y >= 0:
            yield Node(x, y)

    def travel(self, start):
        queue = deque([])
        queue.append(start)
        while queue:
            # pop first node in our queue
            current = queue.popleft()
            # move to next position
            for position in self.walk(current):
                self.values[position] = self.value_of(position)
                queue.append(position)
        return self.values


def answer(grid, offset):
    # build graph
    graph = Graph(grid, offset)
    # find all trees in our offset path
    trees = [p for p in graph.travel(Node(0, 0)) if graph.is_tree(p)]
    return len(trees)
