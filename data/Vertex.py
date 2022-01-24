from dataclasses import dataclass

from . import VertexLabel

@dataclass (init=True, repr=True, unsafe_hash=True)
class Vertex:
    """
Class representing a vertex. It has its coordinates (x, y), unique id and label (from VertexLabel enum).
    """
    x: int
    y: int
    id: int
    label: VertexLabel