"""
Class representing graph fragment - the fragment of graph identified with a vertice from which we can build more graph
fragments on lower layers. This is a middle_vertice (as mostly this vertice is in the middle of graph fragment).
For productions P1 to P6 and P10 you use only one graph fragment in the left side of production.
For other productions you need to choose 2 or more graph fragments by middle vertices for the left side of production,
choose desired vertices, merge them and modify graph fragments to be updated as merged at the graph fragment list.

Squares are the physical 1x1 squares which the fragment occupies.
"""


from typing import List, Tuple
from data.Square import Square
from data.Vertex import Vertex


class GraphFragment:
    def __init__(
        self,
        squares: List[Square],
        vertices: List[Vertex],
        layer_number: int,
        edges: List[Tuple],
        middle_vertex: Vertex,
    ):
        self.squares = squares
        self.vertices = vertices
        self.layer_number = layer_number
        self.edges = edges
        self.middle_vertex = middle_vertex
