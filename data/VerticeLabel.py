from enum import Enum

"""
Enum representing the vertice label
E - an "edge" vertice from which you cannot make any lower part of the graph
I - a middle vertice from which you can make a lower part of the graph
i - a middle vertice from which you cannot make a lower part of the graph as it has already been built
"""


class VerticeLabel(Enum):
    E = 1
    I = 2
    i = 3
    UNDEFINED = 4
