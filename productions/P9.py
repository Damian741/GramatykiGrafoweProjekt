from typing import List
from common import *
from data.VertexLabel import VertexLabel
from util.SortUtils import sort_graph_fragments


def P9(id1, id2, id3, id4):
    global verticies_graph_fragment
    global graph_fragment_list
    graph_fragment_upper_left = verticies_graph_fragment.get(id1)
    graph_fragment_upper_right = verticies_graph_fragment.get(id2)
    graph_fragment_lower_left = verticies_graph_fragment.get(id3)
    graph_fragment_lower_right = verticies_graph_fragment.get(id4)

    if None in [
        graph_fragment_upper_left,
        graph_fragment_upper_right,
        graph_fragment_lower_left,
        graph_fragment_lower_right,
    ]:
        raise Exception(
            "Vertex I labels needed for production 8 are incorrect in graph"
        )

    if (
        set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_lower_right.vertices)
        and set(graph_fragment_upper_right.vertices).isdisjoint(graph_fragment_lower_left.vertices)
        and not set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_upper_right.vertices)
        and not set(graph_fragment_upper_left.vertices).isdisjoint(graph_fragment_lower_left.vertices)
        and not set(graph_fragment_upper_right.vertices).isdisjoint(graph_fragment_lower_right.vertices)
        and not set(graph_fragment_lower_right.vertices).isdisjoint(graph_fragment_lower_left.vertices)
    ):
        print("Mogę być użyty")
        middle_upper_right = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        middle_lower_right = get_upper_right_vertice_in_graph_fragment(graph_fragment_lower_left)
        if middle_upper_right is not middle_lower_right:
            print("Wspólny wierzchołek jest różny po lewej stronie")

        middle_upper_left = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
        middle_lower_left = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_right)
        if middle_upper_left is not middle_lower_left:
            print("Wspólny wierzchołek jest różny po prawej stronie")
        
        if middle_upper_right is not middle_lower_left:
            print("Rozdzielne")

        merge_vertices_to_zero_point(middle_upper_right, middle_upper_left, graph_fragment_list)

        # TODO sprawdzanie jeszcze co gdy nasze przesunięcie jest w górę,
        # aktualny obsługiwany przypadek to sytuacja gdy przesunięcie jest w prawo, patrz ../idea_sketches/P9_case.jpg
        # dodać if sprawdzający czy upper_left.x != upper_right.x - 1 => występuje przesunięcie w prawo?
        # if upper_left.y != lower_left.y - 1 => występuje przesunięcie w dół?
        graph_fragment_modified_list = get_all_connected_graph_fragments_x_sided(graph_fragment_upper_left)
        graph_fragment_modified_list.extend(get_all_connected_graph_fragments_x_sided(graph_fragment_lower_left))

        vertice_left_upper = get_upper_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        vertice_left_lower = get_lower_right_vertice_in_graph_fragment(graph_fragment_lower_left)
        exceptions = [vertice_left_upper.id, vertice_left_lower.id, middle_upper_right.id] # [middle_upper_right.id]
        exceptions.extend(get_vertices_ids_to_the_right(vertice_left_upper))
        exceptions.extend(get_vertices_ids_to_the_right(vertice_left_lower))

        # przesuń wszystkie wierzchołki na prawo od łączenia, po za tymi które sa już poprawne
        for subgraph in graph_fragment_modified_list:
            for vertice in subgraph.vertices:
                if vertice.id not in exceptions:
                    vertice.x -= 1
                    exceptions.append(vertice.id)


        graph_fragment_modified_list = get_all_connected_graph_fragments_y_sided(graph_fragment_upper_left)
        for i in graph_fragment_modified_list:
            print(i.middle_vertex.id)


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