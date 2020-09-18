""" Implementation of the astar algorithm """
from math import inf, sqrt
from src.node import Node

# Two different ways of finding the heuristic
def manhattan_distance(start, end):
    """
    >>> inp: [0,3], [5,5]
    """
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def eucledian_distance(start, end):
    """
    >>> inp: [0,3], [5,5]
    """
    return sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)


def backtrack(current_node):
    """
    When arriving at the end node, 
    find the path by backtracking until arriving at the start node
    """
    path = [current_node.pos]
    while current_node.parent:
        current_node = current_node.parent
        path.append(current_node.pos)
    return path[::-1]

def astar(start, end, map_obj):
    """
    Combines dfs and bfs into a more optimized way of searching
    :param start, list[int], start position
    :param end, list[int], end position
    :param map_obj, Map_Obj, this is to have access to the cell values
    """
    start_node = Node(start, None)
    end_node = Node(end, None)

    start_node.h = manhattan_distance(start, end) 
    start_node.f = start_node.g + start_node.h

    opened = [start_node]
    closed = []

    while opened:
        opened.sort()
        curr_node = opened.pop(0)
        closed.append(curr_node)

        if curr_node.pos == end_node.pos:
            return backtrack(curr_node)
           
         # Generate neighbors for the current node
        (x,y) = curr_node.pos
        neighbors = [[x-1,y],[x,y-1],[x,y+1], [x+1,y]]

        for nxt in neighbors:
            # the map value basically becomes the cost of travelling to that cell
            map_val = map_obj.get_cell_value(nxt)

            # Check if we hit a wall
            if map_val == -1:
                continue

            neighbor = Node(nxt, curr_node)
            if neighbor in closed:
                continue

            neighbor.g = curr_node.g + map_val
            neighbor.h = manhattan_distance(neighbor.pos, end_node.pos)
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(opened, neighbor):
                opened.append(neighbor)

def add_to_open(opened, neighbor):
    """
    Check if neighbor is cheap enough and in the opened list
    """
    for node in opened:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True
