""" This file specifies how nodes are created """

class Node():

    def __init__(self, position=None, parent=None):
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = parent
        self.pos = position

    def __eq__(self, other):
        return self.pos == other.pos
    
    # makes it easier to sort open nodes instead of using lambdas
    def __lt__(self, other):
        return self.f < other.f
