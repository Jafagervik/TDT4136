""" Implementation of the astar algorithm """
from node import Node
from math import abs

def manhattan_distance(start, end):
    return abs(start.x - end.x) + abs(start.y - end.y)

def eucledian_distance(start, end):
    pass


def best_fist_search(start):
    """
    Combines dfs and bfs into a more optimized way of searching
    :param start, Node, start position
    """

    closed_nodes = []
    

    start.g = 0
    start.h = manhattan_distance(start, None) # Erstatt None med end node omsider
    
    start.f = start.g + start.h
    open_nodes = [start]

    while open_nodes:
        x = open.pop()
        closed_nodes.append(x)
        if x == end:
            return True
        
    
    

def astar():
    return
