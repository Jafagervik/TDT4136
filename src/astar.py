""" Implementation of the astar algorithm """
from math import abs, inf
from node import Node
from Map import (
    get_cell_value,
    get_end_goal_pos
)

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def eucledian_distance(start, end):
    return sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)


def astar(start, end, temp=None):
    """
    Combines dfs and bfs into a more optimized way of searching
    :param start, Node, start position
    """
    approved = [',', '.', ';', ':']
    dirs = [[1,0], [0,1], [-1,0], [0,-1]]
    start_node = Node(None, start)
    end_node = Node(None, end)

    start_node.h = manhattan_distance(start, end) # Erstatt None med end node omsider
    start_node.f = start_node.g + start_node.h

    open_nodes = [start_nodes]
    closed_nodes = []
    path = [start_node]

    while open_nodes:
        curr_node = Node(None, open_nodes.pop())
        # G is lowest cost from start to where we are
        # f = g  + h
        curr_node.h = manhattan_distance(curr_node.pos, end_node.pos)

        closed_nodes.append(curr_node)

        if curr == end:
            return reversed(path)

        neighbours = [curr_node.pos += dir for dir in dirs]
        for n in neighbours:
            if get_cell_value(n) != -1 or n in closed_nodes:
                break

            if None:
                g = 0
                h = manhattan_distance(n, end)
                f = g + h

                if n not in open_nodes:
                    open_nodes.append(n)





