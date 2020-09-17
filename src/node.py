""" Here we create the file for the different type of nodes we'll be using """


class Node():

    def __init__(g=0, h=0):
        self.state = None
        self.g = g
        self.h = h
        self.f = self.g + self.h
        self.open = True # status update
        self.parent = None
        self.kids = None

    def __eq__(other):
        return self.state == other.state
