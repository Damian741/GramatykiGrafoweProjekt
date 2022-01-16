from data.Vertex import Vertex
from data.VertexLabel import VertexLabel
from productions.P1 import P1
from productions.P5 import P5
from productions.P2 import P2
from util.GraphDrawer import draw_graph
from common import verticies_graph_fragment
from common import find_vertice_with_coordinates_and_remove_duplicates

def test1():
    """4a 5a"""
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)
    assert verticies_graph_fragment.get(10) != None

def test2():
    """1a 4b 5b"""
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31)]))
    graph_fragment.edges.remove((1, 3))
    P5(5)
    assert verticies_graph_fragment.get(10) == None


def test3():
    """1b 4c"""
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(2, 30), (1, 31), (3, 31), (2, 32), (4,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)
    assert verticies_graph_fragment.get(10) == None

def test4():
    """1c 4d"""
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(2)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)
    assert verticies_graph_fragment.get(10) == None

def test5():
    """1d 2a 5b"""
    P1(0)
    P2(5)
    graph_fragment = verticies_graph_fragment.get(10)
    graph_fragment.vertices.extend(list([Vertex(0.5, -3, 70, VertexLabel(1)), Vertex(0, -3.5, 71, VertexLabel(1)), Vertex(1, -3.5, 72, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(6, 70), (7, 70), (6, 71), (8, 71), (7, 72), (9, 72)]))
    graph_fragment.edges.remove((6, 7))
    graph_fragment.edges.remove((8, 6))
    graph_fragment.edges.remove((7, 9))
    P5(10)
    assert verticies_graph_fragment.get(30) != None

def test6():
    """2b 5c"""
    P1(0)
    P2(5)
    graph_fragment = verticies_graph_fragment.get(10)
    graph_fragment.vertices.extend(list([Vertex(0.5, -3, 70, VertexLabel(1)), Vertex(0, -3.5, 71, VertexLabel(1)), Vertex(1, -3.5, 72, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(6, 70), (7, 70), (6, 71), (8, 71), (7, 72), (9, 72)]))
    graph_fragment.edges.remove((6, 7))
    graph_fragment.edges.remove((8, 6))
    graph_fragment.edges.remove((7, 9))
    P5(10)
    P2(25)
    assert verticies_graph_fragment.get(30) != None

def test7():
    """2c 2d 2e 3a 3b 3d 3e 5d 5e 5f"""
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)

    upper_layer_number = graph_fragment.layer_number
    lower_layer_number = upper_layer_number + 1
    lower_squares = [verticies_graph_fragment.get(x) for x in [10, 15, 20, 25]]
    for s in lower_squares:
        assert s.layer_number == lower_layer_number
    for x in [0, 1, 2]:
        for y in [-3, -4, -5]:
            vertex = find_vertice_with_coordinates_and_remove_duplicates(x, y, lower_squares)
            assert vertex.label == VertexLabel.E
    for x in [0.5, 1.5]:
        for y in [-3.5, -4.5]:
            vertex = find_vertice_with_coordinates_and_remove_duplicates(x, y, lower_squares)
            assert vertex.label == VertexLabel.I

    assert lower_squares[0].edges == [(9, 8), (8, 6), (6, 7), (7, 9), (9, 10), (8, 10), (6, 10), (7, 10)]
    assert lower_squares[1].edges == [(9, 7), (7, 12), (12, 14), (14, 9), (9, 15), (7, 15), (12, 15), (14, 15)]
    assert lower_squares[2].edges == [(18, 8), (8, 9), (9, 19), (19, 18), (18, 20), (8, 20), (19, 20), (9, 20)]
    assert lower_squares[3].edges == [(9, 14), (14, 24), (24, 19), (19, 9), (9, 25), (14, 25), (24, 25), (19, 25)]
    

def test8():
    """4e"""
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.6, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)
    assert verticies_graph_fragment.get(10) == None

def test9():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -2, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(3, 30), (4, 30), (1, 31), (3, 31), (2, 32), (4,32)]))
    graph_fragment.edges.remove((3, 4))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)
    assert verticies_graph_fragment.get(10) != None

def test10():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -2, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(0.5, -1, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(3, 30), (4, 30), (1, 31), (3, 31), (2, 32), (1,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((3, 4))
    P5(5)
    assert verticies_graph_fragment.get(10) != None

def test11():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -2, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(0.5, -1, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(4, 30), (1, 31), (3, 31), (2, 32), (1,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)
    assert verticies_graph_fragment.get(10) == None

def test12():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -2, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(3, 30), (4, 30), (1, 31), (3, 31)]))
    graph_fragment.edges.remove((3, 4))
    graph_fragment.edges.remove((1, 3))
    P5(5)
    assert verticies_graph_fragment.get(10) == None

def test13():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -2, 31, VertexLabel(1)), Vertex(0, -1.5, 30, VertexLabel(1)), Vertex(0.5, -1, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(4, 30), (1, 31), (3, 31), (2, 32), (1,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)
    assert verticies_graph_fragment.get(10) == None

def test14():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(2)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P5(5)
    assert verticies_graph_fragment.get(10) == None
