""" Implementation of the astar algorithm """
from node import Node
from math import abs

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def eucledian_distance(start, end):
    return sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)


def astar(start, end, temp=None):
    """
    Combines dfs and bfs into a more optimized way of searching
    :param start, Node, start position
    """
    [0, 2]


    start.g = 0
    start.h = manhattan_distance(start, None) # Erstatt None med end node omsider

    open_nodes = [start]
    closed_nodes = []

    while open_nodes:
        curr = open_nodes.pop()
        closed_nodes.append(x)
        if curr == end:
            return

        for neighbour in start.children:
            if neighbour not in [(1,0), (0,1), (0, -1), (-1, 0)] or neighbour in closed:
                break

            if None:
                neighbour.f = manhattan_distance((0,0), (4,5))
                neighbour.parent 
