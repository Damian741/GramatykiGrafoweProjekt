from common import *
from data.VertexLabel import VertexLabel
from util.SortUtils import sort_graph_fragments

"""
Ids should be sorted by y and next by x values.
"""


def P7(id1, id2, id3, id4):
    global verticies_graph_fragment
    global graph_fragment_list

    graph_fragment_upper_left = verticies_graph_fragment.get(id1)
    graph_fragment_upper_right = verticies_graph_fragment.get(id2)
    graph_fragment_lower_left = verticies_graph_fragment.get(id3)
    graph_fragment_lower_right = verticies_graph_fragment.get(id4)

    if None in [graph_fragment_upper_left, graph_fragment_upper_right, graph_fragment_lower_left, graph_fragment_lower_right]:
        raise Exception("Vertex I labels needed for production 7 are incorrect in graph")

    if not set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_upper_right.vertices)\
            and not set(graph_fragment_lower_left.vertices).isdisjoint(graph_fragment_lower_right.vertices)\
            and set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_lower_left.vertices)\
            and set(graph_fragment_upper_right.vertices).isdisjoint(graph_fragment_lower_right.vertices):
        top_left_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_left)
        bottom_left_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_left)

        top_middle_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
        bottom_middle_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_right)

        top_right_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_right)
        bottom_right_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_lower_right)

        if None in [top_left_vertex, top_middle_vertex, top_right_vertex, bottom_right_vertex,
                               bottom_middle_vertex, bottom_left_vertex]:
            raise Exception("Some vertex is missing")

        continue_production = check_vertices_labels([top_left_vertex, top_middle_vertex, top_right_vertex, bottom_right_vertex,
                               bottom_middle_vertex, bottom_left_vertex], VertexLabel.E)
        if not continue_production:
            raise Exception("Vertex E labels needed for production 7 are incorrect in graph")

        continue_production = check_vertices_coordinates_horizontal([(top_left_vertex, bottom_left_vertex),
                                               (top_middle_vertex, bottom_middle_vertex),
                                               (top_right_vertex, bottom_right_vertex)])
        if not continue_production:
            raise Exception("Vertex coordinates are wrong for 7 production")

        merge_vertices_to_zero_point(top_left_vertex, bottom_left_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(top_right_vertex, bottom_right_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(top_middle_vertex, bottom_middle_vertex, graph_fragment_list)

        graph_fragment_modified_list = get_all_connected_graph_fragments_y_sided(graph_fragment_upper_left)
        graph_fragment_modified_list.extend(get_all_connected_graph_fragments_y_sided(graph_fragment_upper_right))
        move_vertices_y(graph_fragment_modified_list, [top_right_vertex.id, top_middle_vertex.id, top_left_vertex.id])

    elif not set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_lower_left.vertices)\
            and not set(graph_fragment_upper_right.vertices).isdisjoint(graph_fragment_lower_right.vertices) \
            and set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_upper_right.vertices) \
            and set(graph_fragment_lower_left.vertices).isdisjoint(graph_fragment_lower_right.vertices):
        left_top_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        right_top_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_upper_right)

        left_middle_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        right_middle_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)

        left_bottom_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_lower_left)
        right_bottom_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_lower_right)

        if None in [left_top_vertex, left_middle_vertex, left_bottom_vertex, right_top_vertex,
                               right_middle_vertex, right_bottom_vertex]:
            raise Exception("Some vertex is missing")

        continue_production = check_vertices_labels([left_top_vertex, left_middle_vertex, left_bottom_vertex, right_top_vertex,
                               right_middle_vertex, right_bottom_vertex], VertexLabel.E)
        if not continue_production:
            raise Exception("Vertex E labels needed for production 7 are incorrect in graph")

        continue_production = check_vertices_coordinates_vertical([(left_top_vertex, right_top_vertex),
                                             (left_middle_vertex, right_middle_vertex),
                                             (left_bottom_vertex, right_bottom_vertex)])
        if not continue_production:
            raise Exception("Vertex coordinates are wrong for 7 production")

        merge_vertices_to_zero_point(left_top_vertex, right_top_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(left_middle_vertex, right_middle_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(left_bottom_vertex, right_bottom_vertex, graph_fragment_list)

        graph_fragment_modified_list = get_all_connected_graph_fragments_x_sided(graph_fragment_upper_left)
        graph_fragment_modified_list.extend(get_all_connected_graph_fragments_x_sided(graph_fragment_lower_left))
        move_vertices_x(graph_fragment_modified_list, [left_top_vertex.id, left_middle_vertex.id, left_bottom_vertex.id])

    else:
        raise Exception("Graph is wrongly configured")

    graph_fragment_list.extend(graph_fragment_modified_list)
    sorted_graph_fragment_list = sort_graph_fragments(graph_fragment_list)
    graph_fragment_list.clear()
    graph_fragment_list.extend(sorted_graph_fragment_list)


def merge_vertices_to_zero_point(strong_vertex: Vertex, deleted_vertex: Vertex, graph_fragment_list: List[GraphFragment]):
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
