from productions.P1 import P1
from productions.P2 import P2
from productions.P7 import P7
from common import *
import pytest


def test_p7_working_case():
    prepare_graph()
    P7(40, 45, 90, 95)
    graph_fragment1 = verticies_graph_fragment.get(40)
    graph_fragment2 = verticies_graph_fragment.get(45)
    graph_fragment3 = verticies_graph_fragment.get(90)
    graph_fragment4 = verticies_graph_fragment.get(95)
    graph_fragments = [graph_fragment1, graph_fragment2, graph_fragment3, graph_fragment4]
    amount_vertices = count_vertices_in_graph_fragments(graph_fragments)
    amount_edges_vertices = count_edges_vertices_in_graph_fragments(graph_fragments)
    amount_orange_labeled_vertices = count_orange_vertices_in_graph_fragments(graph_fragments)
    assert amount_vertices == 13 and amount_edges_vertices == 9 and amount_orange_labeled_vertices == 4


def prepare_graph():
    P1(0)
    P2(5)
    P2(10)
    P2(15)
    P2(25)
    P2(20)


def count_vertices_in_graph_fragments(fragments):
    count = set()
    for fragment in fragments:
        for vertex in fragment.vertices:
            count.add(vertex.id)
    return len(count)


def count_edges_vertices_in_graph_fragments(fragments):
    count = set()
    for fragment in fragments:
        for vertex in fragment.vertices:
            if vertex.label == VertexLabel.E:
                count.add(vertex.id)
    return len(count)


def count_orange_vertices_in_graph_fragments(fragments):
    count = set()
    for fragment in fragments:
        for vertex in fragment.vertices:
            if vertex.label == VertexLabel.I:
                count.add(vertex.id)
    return len(count)


def test_p7_missing_vertex():
    prepare_graph()
    graph_fragment1 = verticies_graph_fragment.get(40)
    vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment1)
    graph_fragment1.vertices.remove(vertex)
    with pytest.raises(Exception, match="Some vertex is missing"):
        P7(40, 45, 90, 95)


def test_p7_wrong_labels():
    prepare_graph()
    graph_fragment1 = verticies_graph_fragment.get(40)
    vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment1)
    vertex.label = VertexLabel.I
    with pytest.raises(Exception, match="Vertex E labels needed for production 7 are incorrect in graph"):
        P7(40, 45, 90, 95)


def test_p7_wrong_labels_of_middle_vertices():
    prepare_graph()
    P2(40)
    with pytest.raises(Exception, match="Vertex I labels needed for production 7 are incorrect in graph"):
        P7(40, 45, 90, 95)
