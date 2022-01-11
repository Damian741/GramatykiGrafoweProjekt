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

    if set(graph_fragment_upper_right.vertices).isdisjoint(graph_fragment_lower_right.vertices):
        top_middle_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
        bottom_middle_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_right)

        top_right_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_right)
        bottom_right_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_lower_right)

        merge_vertices_to_zero_point(top_right_vertex, bottom_right_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(top_middle_vertex, bottom_middle_vertex, graph_fragment_list)

    if set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_lower_left.vertices):
        top_left_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_left)
        bottom_left_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_left)

        top_middle_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
        bottom_middle_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_right)

        merge_vertices_to_zero_point(top_left_vertex, bottom_left_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(top_middle_vertex, bottom_middle_vertex, graph_fragment_list)

    if set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_upper_right.vertices):
        top_left_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        top_right_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_upper_right)

        middle_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        middle_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)

        merge_vertices_to_zero_point(top_left_vertex, top_right_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(middle_left_vertex, middle_right_vertex, graph_fragment_list)

    if set(graph_fragment_lower_left.vertices).isdisjoint(graph_fragment_lower_right.vertices):


        middle_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        middle_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)

        bottom_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_lower_left)
        bottom_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_lower_right)

        merge_vertices_to_zero_point(middle_left_vertex, middle_right_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(bottom_left_vertex, bottom_right_vertex, graph_fragment_list)

def merge_vertices_to_zero_point(strong_vertex: Vertex, deleted_vertex: Vertex, graph_fragment_list: []):
    for single_graph_fragment in graph_fragment_list:
        if deleted_vertex in single_graph_fragment.vertices:
            middle_vertex = single_graph_fragment.middle_vertex
            merge_vertices_to_zero_point_single_operation(strong_vertex, deleted_vertex,
                                                          verticies_graph_fragment.get(middle_vertex.id))


def merge_vertices_to_zero_point_single_operation(top_vertex: Vertex, bottom_vertex: Vertex,
                                                  lower_graph_fragment: GraphFragment):
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
