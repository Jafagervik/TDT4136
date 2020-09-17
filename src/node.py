""" Here we create the file for the different type of nodes we'll be using """


class Node():

    def __init__(self, position=None, parent=None):
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = parent
        self.pos = position

    def __eq__(self, other):
        return self.pos == other.pos

    def __lt__(self, other):
        return self.f < other.f
