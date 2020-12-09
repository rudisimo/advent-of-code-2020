from collections import deque
from math import ceil


def expand_grid(grid, offset):
    factor = ceil(len(grid) / offset.y) + 1
    return [list(r) * factor for r in grid]


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
        return f"Node({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


class Graph:
    TYPE_OPEN = "."
    TYPE_TREE = "#"

    def __init__(self, grid, offset):
        self.grid = expand_grid(grid, offset)
        self.offset = offset
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.visited = set()
        self.values = {}

    def value_of(self, node):
        return self.grid[node.y][node.x]

    def is_tree(self, node):
        return self.value_of(node) == self.TYPE_TREE

    def walk(self, node, offset):
        x, y = list(tuple(u + v for u, v in zip((node.x, node.y), offset)))
        if self.width > x >= 0 and self.height > y >= 0:
            yield Node(x, y)

    def travel(self):
        queue = deque([])
        queue.append(Node(0, 0))

        while queue:
            current = queue.popleft()
            self.visited.add(current)

            for next in self.walk(current, self.offset):
                self.values[next] = self.value_of(next)
                queue.append(next)

        return self.values


def answer(grid, offset):
    graph = Graph(grid, offset)
    trees = [p for p in graph.travel() if graph.is_tree(p)]
    return len(trees)
