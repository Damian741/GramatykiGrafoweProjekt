from pytest import raises

from common import verticies_graph_fragment as vertice_graph_fragment
from data import MisconfiguredGraph, VertexLabel
from productions import P9


def test_basic_graph_for_P9 (basic_graph_for_P9):
    assert vertice_graph_fragment


def test__merge_vertical__shift_left__graph (merge_vertical__shift_left__graph):
    P9 (355, 370, 365, 380)

    assert vertice_graph_fragment
    assert 368 not in [vertex.id for vertex in vertice_graph_fragment [370].vertices]


def test__merge_horizontal__shift_up (merge_horizontal__shift_up__graph):
    P9 (360, 365, 390, 395)

    assert vertice_graph_fragment
    assert 487 not in [vertex.id for vertex in vertice_graph_fragment [395].vertices]


def test_trashy_vertice (merge_horizontal__shift_up__graph):
    with raises (MisconfiguredGraph):
        P9 (355, 365, 390, 395)


def test_middle_vertice_are_connected (merge_horizontal__shift_up__graph):
    with raises (AttributeError):
        vertice_graph_fragment [360].vertices.pop (1)
        P9 (360, 365, 390, 395)


def test_wrong_label (merge_horizontal__shift_up__graph):
    with raises (Exception, match="Vertex 365 has diffrent label then VertexLabel.I"):
        vertice_graph_fragment [365].middle_vertex.label = VertexLabel.E
        P9 (360, 365, 390, 395)