"""
Class representing a vertex. It has its coordinates (x, y), unique id and label (from VertexLabel enum).
"""


from data.VertexLabel import VertexLabel


class Vertex:
    def __init__(self, x, y, id, label: VertexLabel):
        self.x = x
        self.y = y
        self.id = id
        self.label = label
