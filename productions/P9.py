from typing import List, Dict

from common import *
from data import Vertex, GraphFragment, MisconfiguredGraph


## TODO walidacja czy graf lewej strony wygląda tak jak powinien, czyli czy są wszystkie krawędzie, oraz etykiety się zgadzają
def P9 (id1: int, id2: int, id3: int, id4: int, verticies_graph_fragment: Dict = verticies_graph_fragment, graph_fragment_list: List = graph_fragment_list):
    try:
        graph_fragment_upper_left = verticies_graph_fragment [id1]
        graph_fragment_upper_right = verticies_graph_fragment [id2]
        graph_fragment_lower_left = verticies_graph_fragment [id3]
        graph_fragment_lower_right = verticies_graph_fragment [id4]
    except IndexError:
        raise Exception(
            "Vertex I labels needed for production 9 are incorrect in graph"
        )

    if not (
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
        raise MisconfiguredGraph ()

    if (
        graph_fragment_upper_left.middle_vertex.x
        == graph_fragment_upper_right.middle_vertex.x - 2
        and graph_fragment_lower_left.middle_vertex.x
        == graph_fragment_lower_right.middle_vertex.x - 2
    ):
        validate_graph(
            graph_fragment_upper_left,
            graph_fragment_upper_right,
            graph_fragment_lower_left,
            graph_fragment_lower_right,
        )
        middle_upper_right = get_lower_right_vertice_in_graph_fragment(
            graph_fragment_upper_left
        )
        middle_lower_right = get_upper_right_vertice_in_graph_fragment(
            graph_fragment_lower_left
        )
        if middle_upper_right is not middle_lower_right:
            raise Exception("Middle vertex on right side is not connected")

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
        validate_graph(
            graph_fragment_upper_right,
            graph_fragment_lower_right,
            graph_fragment_upper_left,
            graph_fragment_lower_left,
            orient="V",
        )
        print("Przesunięcie w pionie?")
        middle_upper_left = get_lower_right_vertice_in_graph_fragment(
            graph_fragment_upper_left
        )
        middle_upper_right = get_lower_left_vertice_in_graph_fragment(
            graph_fragment_upper_right
        )
        if middle_upper_left is not middle_upper_right:
            raise Exception("Middle vertex on upper side is not connected")

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
            for vertex in subgraph.vertices:
                if vertex.id not in exceptions:
                    vertex.x -= 1
                    exceptions.append(vertex.id)

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
            for vertex in subgraph.vertices:
                if vertex.id not in exceptions:
                    vertex.y += 1
                    exceptions.append(vertex.id)

    else:
        raise MisconfiguredGraph ()



## podajemy podgrafy tak aby zszywanie było pionowe (rozłączone prawo-lewo)
def validate_graph(
    graph_fragment_upper_left,
    graph_fragment_upper_right,
    graph_fragment_lower_left,
    graph_fragment_lower_right,
    orient="H",
):
    print("Validate")
    check_vertex_labels(
        [
            graph_fragment_upper_left.middle_vertex,
            graph_fragment_upper_right.middle_vertex,
            graph_fragment_lower_left.middle_vertex,
            graph_fragment_lower_right.middle_vertex,
        ],
        VertexLabel.I,
    )

    if orient == "H":
        ## ten wierzchołek powinien być wspólny dla lewego i prawego górnego podgrafu
        upper_left_vertex = get_upper_right_vertice_in_graph_fragment(
            graph_fragment_upper_left
        )
        ## wspólny dla lewego i prawego dolnego podgrafu
        lower_left_vertex = get_lower_right_vertice_in_graph_fragment(
            graph_fragment_lower_left
        )
        ## wspólny dla lewego górnego i dolnego podgrafu
        middle_left_vertex = get_upper_right_vertice_in_graph_fragment(
            graph_fragment_lower_left
        )
        ## wspólny dla prawego górnego i dolnego podgrafu
        middle_right_vertex = get_upper_left_vertice_in_graph_fragment(
            graph_fragment_lower_right
        )
    elif orient == "V":
        upper_left_vertex = get_lower_right_vertice_in_graph_fragment(
            graph_fragment_upper_left
        )
        lower_left_vertex = get_lower_left_vertice_in_graph_fragment(
            graph_fragment_lower_left
        )
        middle_left_vertex = get_lower_right_vertice_in_graph_fragment(
            graph_fragment_lower_left
        )
        middle_right_vertex = get_upper_right_vertice_in_graph_fragment(
            graph_fragment_lower_right
        )

    check_lower_level_edges(
        upper_left_vertex, graph_fragment_upper_left, graph_fragment_upper_right
    )
    check_lower_level_edges(
        lower_left_vertex, graph_fragment_lower_left, graph_fragment_lower_right
    )
    check_lower_level_edges(
        middle_left_vertex, graph_fragment_lower_left, graph_fragment_upper_left
    )
    check_lower_level_edges(
        middle_right_vertex, graph_fragment_lower_right, graph_fragment_upper_right
    )

    check_vertex_labels(
        [upper_left_vertex, lower_left_vertex, middle_left_vertex, middle_right_vertex],
        VertexLabel.E,
    )
    left_upper_id = graph_fragment_upper_left.middle_vertex.id
    left_lower_id = graph_fragment_lower_left.middle_vertex.id
    right_upper_id = graph_fragment_upper_right.middle_vertex.id
    right_lower_id = graph_fragment_lower_right.middle_vertex.id
    left_childs = [left_upper_id, left_lower_id]
    right_childs = [right_upper_id, right_lower_id]
    left_parent_edges = []
    right_parent_edges = []

    # search for parent for I vertices
    for id1, id2 in inter_layer_connections:
        if id1 in left_childs or id2 in left_childs:
            left_parent_edges.append((id1, id2))
        elif id1 in right_childs or id2 in right_childs:
            right_parent_edges.append((id1, id2))

    left_parent_id = check_parent_edges(left_parent_edges, left_upper_id, left_lower_id)
    right_parent_id = check_parent_edges(
        right_parent_edges, right_upper_id, right_lower_id
    )
    for graph_fragment in graph_fragment_list:
        if graph_fragment.middle_vertex.id == left_parent_id:
            left_parent_graph_fragment = graph_fragment
        elif graph_fragment.middle_vertex.id == right_parent_id:
            right_parent_graph_fragment = graph_fragment
    if None in [left_parent_graph_fragment, right_parent_graph_fragment]:
        raise Exception("Parent/s for left or right side not found")
    check_vertex_labels(
        [
            left_parent_graph_fragment.middle_vertex,
            right_parent_graph_fragment.middle_vertex,
        ],
        VertexLabel.i,
    )
    intersection = set(left_parent_graph_fragment.vertices).intersection(
        right_parent_graph_fragment.vertices
    )
    if not any([vertex.label == VertexLabel.E for vertex in intersection]):
        raise Exception("Parents not connected by vertex with E label")
    if not any(
        check_edges(
            intersection,
            left_parent_graph_fragment.middle_vertex,
            left_parent_graph_fragment,
        )
    ) or not any(
        check_edges(
            intersection,
            left_parent_graph_fragment.middle_vertex,
            left_parent_graph_fragment,
        )
    ):
        raise Exception("Parents not connected by edges with vertex with E label")


def check_edges(vertices, parent, graph_fragment):
    return [
        (vertex.id, parent.id) in graph_fragment.edges
        or (parent.id, vertex.id) in graph_fragment.edges
        for vertex in vertices
    ]


def check_lower_level_edges(vertex, graph_fragment_base, graph_fragment_other):
    if (
        vertex not in graph_fragment_other.vertices
        or not any(
            check_edges(
                [vertex], graph_fragment_base.middle_vertex, graph_fragment_base
            )
        )
        or not any(
            check_edges(
                [vertex], graph_fragment_other.middle_vertex, graph_fragment_other
            )
        )
    ):
        raise Exception(
            f"{graph_fragment_base.middle_vertex.id} and {graph_fragment_other.middle_vertex.id} dont have connected vertice with {vertex.id}"
        )


def check_parent_edges(parent_edges, upper_id, lower_id):
    if len(parent_edges) != 2:
        raise Exception(
            f"There is {len(parent_edges)} edges connected with {upper_id} or/and {lower_id}. Should be only 2"
        )
    for id1, id2 in parent_edges:
        if id1 == upper_id:
            upper_parent = id2
        elif id2 == upper_id:
            upper_parent = id1
        elif id1 == lower_id:
            lower_parent = id2
        elif id2 == lower_id:
            lower_parent = id1
    if upper_parent != lower_parent:
        raise Exception(
            f"Graph fragment {lower_id} and {upper_id} have diffrent parents: {upper_parent} and {lower_parent}"
        )
    return upper_parent


def check_vertex_labels(vertexes, label):
    for vertex in vertexes:
        if not vertex.label == label:
            raise Exception(f"Vertex {vertex.id} has diffrent label then {label}")


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
