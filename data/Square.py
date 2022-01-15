"""
Class representing single (indivisible) 1x1 square
Field id is not the same as vertex id. Vertex id is unique in the whole graph and field id identifies each square within
a layer - on layer 0 you have 1 square with field id 0, on layer 1 you have 4 squares with field ids 0-3, on layer 2 you have
16 squares with field ids 0-15 and so on...
"""


class Square:
    def __init__(self, field_id: int, layer_number: int):
        self.field_id = field_id
        self.layer_number = layer_number
        self.vertices = []
