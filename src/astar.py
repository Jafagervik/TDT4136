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


def backtrack(current_node):
    path = [current_node.pos]
    while current_node.parent:
        current_node = current_node.parent
        path.append(current_node.pos)
    return path[::-1]

def astar(start, end, temp=None):
    """
    Combines dfs and bfs into a more optimized way of searching
    :param start, Node, start position
    """
    start_node = Node(start, None)
    end_node = Node(end, None)

    start_node.h = manhattan_distance(start, end) # Erstatt None med end node omsider
    start_node.f = start_node.g + start_node.h

    opened = [start_node]
    closed = []

    while opened:
        opened.sort()
        curr_node = opened.pop(0)
        closed.append(curr_node)

        closed_nodes.append(curr_node)

        if curr_node.pos == end_node.pos:
            return backtrack(curr)
        (x,y) = curr_node.pos
        neighbors = [(x-1,y),(x,y-1),(x,y+1),(x+1,y)]


        for nxt in neighbors:
            map_val = get_cell_value(nxt)

            # Do we hit a wall
            if (get_cell_value) == "#":
                continue

            # Check boundaries
            neighbor = Node(nxt, curr_node)
            if neighbor in closed:
                continue

            neighbor.g = manhattan_distance(neighbor.pos, end_node.pos)
            neighbor.h = manhattan_distance(neighbor.pos, end_node.pos)
            neighbor.f = neighbor.g + neighbor.h

            opened.append(neighbor) if add_to_open(opened, neighbor):

def add_to_open(opened, neighbor):
    for node in opened:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True
