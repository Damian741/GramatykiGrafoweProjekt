from enum import Enum

"""
Enum representing the vertex label
E - an "edge" vertex from which you cannot make any lower part of the graph
I - a middle vertex from which you can make a lower part of the graph
i - a middle vertex from which you cannot make a lower part of the graph as it has already been built
"""


class VertexLabel(Enum):
    E = 1
    I = 2
    i = 3
    UNDEFINED = 4
