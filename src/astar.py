""" Implementation of the astar algorithm """
from node import Node
from math import abs

def manhattan_distance(start, end):
    return abs(start.x - end.x) + abs(start.y - end.y)

def eucledian_distance(start, end):
    pass

def shortest(x, y):
    pass


def best_fist_search(start):
    """
    Combines dfs and bfs into a more optimized way of searching
    :param start, Node, start position
    """



    start.g = 0
    start.h = manhattan_distance(start, None) # Erstatt None med end node omsider

    start.f = start.g + start.h
    open_nodes = [start]
    closed_nodes = []

    while open_nodes:
        x = open_nodes.pop()
        closed_nodes.append(x)
        if x == end:
            return

        for neighbour in start.children:
            if neighbour not in dirs or neighbourn in closed:
                break

            if None:
                neighbour.f = manhattan_distance((0,0), (4,5))
                neighbour.parent


def astar():
    return
