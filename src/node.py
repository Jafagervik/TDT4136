""" Here we create the file for the different type of nodes we'll be using """


class Node():

    def __init__(self, g=0, h=0):
        self.state = None
        self.g = g
        self.h = h
        self.f = self.g + self.h
        self.parent = None
        self.kids = None

    def __eq__(self, other):
        return self.state == other.state
