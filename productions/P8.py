from common import *
from data.VertexLabel import VertexLabel
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
    print(graph_fragment_upper_left.vertices)
    for v in graph_fragment_upper_left.vertices:
        print(v.x, v.y, v.id)

    top_left_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_left)
    print(top_left_vertex.x, top_left_vertex.y, top_left_vertex.id)

    bottom_left_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_left)
    print(bottom_left_vertex.x, bottom_left_vertex.y, bottom_left_vertex.id)
    
    top_middle_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)

    bottom_middle_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_right)

    top_right_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_right)

    bottom_right_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_lower_right)


    merge_verticies_to_upper(top_left_vertex, bottom_left_vertex, graph_fragment_lower_left)
    merge_verticies_to_upper(top_right_vertex, bottom_right_vertex, graph_fragment_lower_right)
    merge_verticies_to_upper(top_middle_vertex, bottom_middle_vertex, graph_fragment_lower_left)

def merge_verticies_to_upper(top_vertex : Vertex, bottom_vertex : Vertex, lower_graph_fragment : GraphFragment):
    bottom_vertex.y = top_vertex.y
    print(lower_graph_fragment.edges)

    to_remove = []
    to_append = []
    for (a, b) in lower_graph_fragment.edges:
        if a == bottom_vertex.id:
            to_remove.append((bottom_vertex.id, b))
            to_append.append((top_vertex.id, b))
        if b == bottom_vertex.id:
            to_remove.append((a, bottom_vertex.id))
            to_append.append((a, top_vertex.id))
    print(to_remove)

    for t in to_remove:
        lower_graph_fragment.edges.remove(t)
    for t in to_append:
        lower_graph_fragment.edges.append(t)

    print(lower_graph_fragment.edges)

    lower_graph_fragment.vertices.remove(bottom_vertex)
    lower_graph_fragment.vertices.append(top_vertex)
