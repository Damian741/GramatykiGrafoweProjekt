"""
Class representing a vertice. It has its coordinates (x, y), unique id and label (from VerticeLabel enum).
"""


class Vertice:
    def __init__(self, x, y, id, label):
        self.x = x
        self.y = y
        self.id = id
        self.label = label
