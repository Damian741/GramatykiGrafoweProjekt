from common import *
from data.VerticeLabel import VerticeLabel
from util.SortUtils import sort_graph_fragments


def P8(id1, id2, id3, id4):
    global verticies_graph_fragment
    global graph_fragment_list
    graph_fragment_upper_left = verticies_graph_fragment.get(id1)
    graph_fragment_upper_right = verticies_graph_fragment.get(id2)
    graph_fragment_lower_left = verticies_graph_fragment.get(id3)
    graph_fragment_lower_right = verticies_graph_fragment.get(id4)
    print(graph_fragment_upper_left)
    print(graph_fragment_upper_right)
    print(graph_fragment_lower_left)
    print(graph_fragment_lower_right)
    print(graph_fragment_upper_left.verticies)
    for v in graph_fragment_upper_left.verticies:
        print(v.x, v.y, v.id)

    vertice_id1 = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_left.verticies)
    print(vertice_id1.x, vertice_id1.y, vertice_id1.id)

    vertice_id2 = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_left.verticies)
    print(vertice_id2.x, vertice_id2.y, vertice_id2.id)
    vertice_id2.y = vertice_id1.y

    print(graph_fragment_lower_left.edges)

    to_remove = []
    to_append = []
    for (a, b) in graph_fragment_lower_left.edges:
        if a == vertice_id2.id:
            to_remove.append((vertice_id2.id, b))
            to_append.append((vertice_id1.id, b))
        if b == vertice_id2.id:
            to_remove.append((a, vertice_id2.id))
            to_append.append((a, vertice_id1.id))
    print(to_remove)

    for t in to_remove:
        graph_fragment_lower_left.edges.remove(t)
    for t in to_append:
        graph_fragment_lower_left.edges.append(t)
    # graph_fragment_lower_left.edges.remove
    print(graph_fragment_lower_left.edges)

    graph_fragment_lower_left.verticies.remove(vertice_id2)
    graph_fragment_lower_left.verticies.append(vertice_id1)


