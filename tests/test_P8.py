from productions.P1 import P1
from productions.P2 import P2
from productions.P7 import P7
from productions.P8 import P8
from common import *
import pytest


def prepare_basic_graph():
    P1(0)
    P2(5)
    P2(10)
    P2(15)
    P2(25)
    P2(20)


def prepare_case2_graph():
    prepare_basic_graph()
    P7(35, 50, 45, 60)
    P7(95, 70, 105, 80)
    P7(60, 65, 70, 75)


def test_p8_working_case1():
    prepare_basic_graph()
    P7(35, 50, 45, 60)
    P7(95, 70, 105, 80)
    P7(40, 45, 90, 95)
    P8(60, 65, 70, 75)
    graph_fragment1 = verticies_graph_fragment.get(60)
    graph_fragment2 = verticies_graph_fragment.get(65)
    graph_fragment3 = verticies_graph_fragment.get(70)
    graph_fragment4 = verticies_graph_fragment.get(75)
    graph_fragments = [graph_fragment1, graph_fragment2, graph_fragment3, graph_fragment4]
    amount_vertices = count_vertices_in_graph_fragments(graph_fragments)
    amount_edges_vertices = count_edges_vertices_in_graph_fragments(graph_fragments)
    amount_orange_labeled_vertices = count_orange_vertices_in_graph_fragments(graph_fragments)
    assert amount_vertices == 13 and amount_edges_vertices == 9 and amount_orange_labeled_vertices == 4


def test_p8_working_case2():
    prepare_case2_graph()
    P8(40, 45, 90, 95)
    graph_fragment1 = verticies_graph_fragment.get(40)
    graph_fragment2 = verticies_graph_fragment.get(45)
    graph_fragment3 = verticies_graph_fragment.get(90)
    graph_fragment4 = verticies_graph_fragment.get(95)
    graph_fragments = [graph_fragment1, graph_fragment2, graph_fragment3, graph_fragment4]
    amount_vertices = count_vertices_in_graph_fragments(graph_fragments)
    amount_edges_vertices = count_edges_vertices_in_graph_fragments(graph_fragments)
    amount_orange_labeled_vertices = count_orange_vertices_in_graph_fragments(graph_fragments)
    assert amount_vertices == 13 and amount_edges_vertices == 9 and amount_orange_labeled_vertices == 4


def test_p8_working_case3():
    prepare_basic_graph()
    P7(40, 45, 90, 95)
    P7(60, 65, 70, 75)
    P7(95, 70, 105, 80)
    P8(35, 50, 45, 60)
    graph_fragment1 = verticies_graph_fragment.get(35)
    graph_fragment2 = verticies_graph_fragment.get(50)
    graph_fragment3 = verticies_graph_fragment.get(45)
    graph_fragment4 = verticies_graph_fragment.get(60)
    graph_fragments = [graph_fragment1, graph_fragment2, graph_fragment3, graph_fragment4]
    amount_vertices = count_vertices_in_graph_fragments(graph_fragments)
    amount_edges_vertices = count_edges_vertices_in_graph_fragments(graph_fragments)
    amount_orange_labeled_vertices = count_orange_vertices_in_graph_fragments(graph_fragments)
    assert amount_vertices == 13 and amount_edges_vertices == 9 and amount_orange_labeled_vertices == 4


def test_p8_working_case4():
    prepare_basic_graph()
    P7(40, 45, 90, 95)
    P7(60, 65, 70, 75)
    P7(35, 50, 45, 60)
    P8(95, 70, 105, 80)
    graph_fragment1 = verticies_graph_fragment.get(95)
    graph_fragment2 = verticies_graph_fragment.get(70)
    graph_fragment3 = verticies_graph_fragment.get(105)
    graph_fragment4 = verticies_graph_fragment.get(80)
    graph_fragments = [graph_fragment1, graph_fragment2, graph_fragment3, graph_fragment4]
    amount_vertices = count_vertices_in_graph_fragments(graph_fragments)
    amount_edges_vertices = count_edges_vertices_in_graph_fragments(graph_fragments)
    amount_orange_labeled_vertices = count_orange_vertices_in_graph_fragments(graph_fragments)
    assert amount_vertices == 13 and amount_edges_vertices == 9 and amount_orange_labeled_vertices == 4


def test_p8_missing_vertex():
    prepare_case2_graph()
    graph_fragment1 = verticies_graph_fragment.get(40)
    vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment1)
    graph_fragment1.vertices.remove(vertex)
    with pytest.raises(Exception, match="Some vertex is missing"):
        P8(40, 45, 90, 95)


def test_p8_wrong_labels():
    prepare_case2_graph()
    graph_fragment1 = verticies_graph_fragment.get(40)
    vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment1)
    vertex.label = VertexLabel.I
    with pytest.raises(Exception, match="Vertex E labels needed for production 8 are incorrect in graph"):
        P8(40, 45, 90, 95)


def test_p8_wrong_labels_of_middle_vertices():
    prepare_case2_graph()
    P2(40)
    with pytest.raises(Exception, match="Vertex I labels needed for production 8 are incorrect in graph"):
        P8(40, 45, 90, 95)


def test_p8_not_merged_vertex():
    prepare_basic_graph()
    with pytest.raises(Exception, match="Graph is wrongly configured"):
        P8(95, 70, 105, 80)


def test_p8_not_merged_vertex_vertical():
    prepare_basic_graph()
    with pytest.raises(Exception, match="Graph is wrongly configured"):
        P8(60, 65, 70, 75)


def test_p8_wrong_vertex_coordinates():
    prepare_case2_graph()
    with pytest.raises(Exception, match="Vertex coordinates are wrong for 8 production"):
        P8(35, 45, 70, 80)


def test_p8_wrong_vertex_coordinates_vertical():
    prepare_case2_graph()
    with pytest.raises(Exception, match="Vertex coordinates are wrong for 8 production"):
        P8(40, 45, 70, 75)


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
