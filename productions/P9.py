from typing import List
from common import *


## TODO walidacja czy graf lewej strony wygląda tak jak powinien, czyli czy są wszystkie krawędzie, oraz etykiety się zgadzają
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
            "Vertex I labels needed for production 9 are incorrect in graph"
        )

    if (
        set(graph_fragment_upper_left.vertices).isdisjoint(
            graph_fragment_lower_right.vertices
        )
        and set(graph_fragment_upper_right.vertices).isdisjoint(
            graph_fragment_lower_left.vertices
        )
        and not set(graph_fragment_upper_left.vertices).isdisjoint(
            graph_fragment_upper_right.vertices
        )
        and not set(graph_fragment_upper_left.vertices).isdisjoint(
            graph_fragment_lower_left.vertices
        )
        and not set(graph_fragment_upper_right.vertices).isdisjoint(
            graph_fragment_lower_right.vertices
        )
        and not set(graph_fragment_lower_right.vertices).isdisjoint(
            graph_fragment_lower_left.vertices
        )
    ):
        if (
            graph_fragment_upper_left.middle_vertex.x
            == graph_fragment_upper_right.middle_vertex.x - 2
            and graph_fragment_lower_left.middle_vertex.x
            == graph_fragment_lower_right.middle_vertex.x - 2
        ):
            middle_upper_right = get_lower_right_vertice_in_graph_fragment(
                graph_fragment_upper_left
            )
            middle_lower_right = get_upper_right_vertice_in_graph_fragment(
                graph_fragment_lower_left
            )
            if middle_upper_right is not middle_lower_right:
                raise Exception("Middle vertex on right side is not connected")

            middle_upper_left = get_lower_left_vertice_in_graph_fragment(
                graph_fragment_upper_right
            )
            middle_lower_left = get_upper_left_vertice_in_graph_fragment(
                graph_fragment_lower_right
            )
            if middle_upper_left is not middle_lower_left:
                raise Exception("Middle vertex on left side is not connected")

            print(f"Do połączenia: {middle_lower_left.id} z {middle_upper_right.id}")

            merge_vertices_to_zero_point(
                middle_upper_right, middle_upper_left, graph_fragment_list
            )
            graph_fragment_modified_list = get_all_connected_graph_fragments_x_sided(
                graph_fragment_upper_left
            )
            graph_fragment_modified_list.extend(
                get_all_connected_graph_fragments_x_sided(graph_fragment_lower_left)
            )

            vertice_left_upper = get_upper_right_vertice_in_graph_fragment(
                graph_fragment_upper_left
            )
            vertice_left_lower = get_lower_right_vertice_in_graph_fragment(
                graph_fragment_lower_left
            )
            exceptions = [
                vertice_left_upper.id,
                vertice_left_lower.id,
                middle_upper_right.id,
            ]
            exceptions.extend(get_vertices_ids_to_the_right(vertice_left_upper))
            exceptions.extend(get_vertices_ids_to_the_right(vertice_left_lower))

            for subgraph in graph_fragment_modified_list:
                for vertice in subgraph.vertices:
                    if vertice.id not in exceptions:
                        vertice.x -= 1
                        exceptions.append(vertice.id)

        elif (
            graph_fragment_upper_left.middle_vertex.y
            == graph_fragment_lower_left.middle_vertex.y + 2
            and graph_fragment_upper_right.middle_vertex.y
            == graph_fragment_lower_right.middle_vertex.y + 2
        ):
            print("Przesunięcie w pionie?")
            middle_upper_left = get_lower_right_vertice_in_graph_fragment(
                graph_fragment_upper_left
            )
            middle_upper_right = get_lower_left_vertice_in_graph_fragment(
                graph_fragment_upper_right
            )
            if middle_upper_left is not middle_upper_right:
                raise Exception("Middle vertex on upper side is not connected")

            middle_lower_left = get_upper_right_vertice_in_graph_fragment(
                graph_fragment_lower_left
            )
            middle_lower_right = get_upper_left_vertice_in_graph_fragment(
                graph_fragment_lower_right
            )
            if middle_lower_right is not middle_lower_left:
                raise Exception("Middle vertex on lower side is not connected")

            if middle_upper_left is not middle_lower_left:
                print(f"Do połączenia: {middle_upper_left.id} z {middle_lower_left.id}")

            merge_vertices_to_zero_point(
                middle_upper_left, middle_lower_left, graph_fragment_list
            )

            graph_fragment_modified_list = get_all_connected_graph_fragments_y_sided(
                graph_fragment_upper_left
            )
            graph_fragment_modified_list.extend(
                get_all_connected_graph_fragments_y_sided(graph_fragment_upper_right)
            )

            vertice_left_upper = get_upper_left_vertice_in_graph_fragment(
                graph_fragment_upper_left
            )
            vertice_right_upper = get_lower_right_vertice_in_graph_fragment(
                graph_fragment_upper_right
            )
            exceptions = [
                vertice_left_upper.id,
                vertice_right_upper.id,
                middle_upper_left.id,
            ]
            exceptions.extend(get_vertices_ids_to_the_bottom(vertice_left_upper))
            exceptions.extend(get_vertices_ids_to_the_bottom(vertice_right_upper))

            for subgraph in graph_fragment_modified_list:
                for vertice in subgraph.vertices:
                    if vertice.id not in exceptions:
                        vertice.y += 1
                        exceptions.append(vertice.id)

        else:
            raise Exception("Graph is wrongly configured")
    else:
        raise Exception("Graph is wrongly configured")


def merge_vertices_to_zero_point(
    strong_vertex: Vertex,
    deleted_vertex: Vertex,
    graph_fragment_list: List[GraphFragment],
):
    for single_graph_fragment in graph_fragment_list:
        if deleted_vertex in single_graph_fragment.vertices:
            middle_vertex = single_graph_fragment.middle_vertex
            merge_vertices_to_zero_point_single_operation(
                strong_vertex,
                deleted_vertex,
                verticies_graph_fragment.get(middle_vertex.id),
            )


def merge_vertices_to_zero_point_single_operation(
    top_vertex: Vertex, bottom_vertex: Vertex, lower_graph_fragment: GraphFragment
):
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
