from common import *
from data.VertexLabel import VertexLabel
from util.SortUtils import sort_graph_fragments

def P6(id):
    global vertices_graph_fragment
    global graph_fragment_list
    graph_fragment = verticies_graph_fragment.get(id) # check if a graph fragment is registered as possible to extend to lower layers
    
    real_id = graph_fragment.middle_vertex.id

    if len(graph_fragment.vertices) != 9:
        return

    def adjacency_lists(edges):
        def count_edges(edges, d):
            if len(edges) > 0:
                (i, j), *tail = edges
                return count_edges(tail, {**d, i: d.get(i, []) + [j], j: d.get(j, []) + [i]})
            else:
                return d
        return count_edges(edges, {})

    al = adjacency_lists(graph_fragment.edges)

    not_connected = [key for key, value in al.items() if real_id not in value and key != real_id]

    if len(not_connected) != 4:
        return

    reduced_al = { key: al[key] for key in not_connected }

    if [key for key, values in reduced_al.items() if len(values) != 2] != []:
        return

    for key, value in reduced_al.items():
        middle = [x for x in graph_fragment.vertices if x.id == key][0]
        left = [x for x in graph_fragment.vertices if x.id == value[0]][0]
        right = [x for x in graph_fragment.vertices if x.id == value[1]][0]

        if middle.x != (left.x + right.x) / 2:
            return

        if middle.y != (left.y + right.y) / 2:
            return   


    lower_layer_squares = resolve_lower_layer_squares(graph_fragment) # get squares which a new fragment on lower level will occupy
    lower_left_vertice = find_lower_left_vertice(lower_layer_squares) # find the edge lowest vertice on the left
    lower_graph_fragment_width = math.sqrt(len(lower_layer_squares)) # length of a whole square (consisting of small squares) which the new graph fragment occupies
    middle_left_vertice_y = lower_left_vertice.y + lower_graph_fragment_width / 2
    upper_left_vertice_y = lower_left_vertice.y + lower_graph_fragment_width
    lower_middle_vertice_x = lower_left_vertice.x + lower_graph_fragment_width / 2
    lower_right_vertice_x = lower_left_vertice.x + lower_graph_fragment_width
    upper_right_square_middle_x = lower_middle_vertice_x + lower_graph_fragment_width / 4
    upper_right_square_middle_y = middle_left_vertice_y + lower_graph_fragment_width / 4
    lower_right_square_middle_y = lower_left_vertice.y + lower_graph_fragment_width / 4
    upper_left_square_middle_x = lower_left_vertice.x + lower_graph_fragment_width / 4

    lower_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_vertice_x, lower_left_vertice.y, lower_layer_squares) # define new graph fragment vertices coordinates
    upper_left_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_left_vertice.x, upper_left_vertice_y, lower_layer_squares)
    upper_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_vertice_x, upper_left_vertice_y, lower_layer_squares)
    middle_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_middle_vertice_x, middle_left_vertice_y, lower_layer_squares)
    middle_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_vertice_x, middle_left_vertice_y, lower_layer_squares)
    middle_left_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_left_vertice.x, middle_left_vertice_y, lower_layer_squares)
    upper_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_middle_vertice_x, upper_left_vertice_y, lower_layer_squares)
    lower_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_middle_vertice_x, lower_left_vertice.y, lower_layer_squares)

    upper_right_square_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_right_square_middle_x, upper_right_square_middle_y, lower_layer_squares)
    lower_right_square_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_right_square_middle_x, lower_right_square_middle_y, lower_layer_squares)
    upper_left_square_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_left_square_middle_x, upper_right_square_middle_y, lower_layer_squares)
    lower_left_square_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_left_square_middle_x, lower_right_square_middle_y, lower_layer_squares)

    upper_left_square = None
    upper_right_square = None
    lower_left_square = None
    lower_right_square = None


    for square in lower_layer_squares:
        if upper_left_square == None or square.field_id < upper_left_square.field_id:
            upper_left_square = square
    layer_size = (2 ** upper_left_square.layer_number)
    # identification of squares for each new graph fragment
    for square in lower_layer_squares:
        if upper_right_square is None and square.field_id == upper_left_square.field_id + lower_graph_fragment_width / 2:
            upper_right_square = square
        if lower_left_square is None and square.field_id == upper_left_square.field_id + (lower_graph_fragment_width / 2) * layer_size:
            lower_left_square = square
        if lower_right_square is None and square.field_id == (upper_left_square.field_id + (lower_graph_fragment_width / 2) * layer_size) + lower_graph_fragment_width / 2:
            lower_right_square = square
    upper_left_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, upper_left_square)
    upper_right_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, upper_right_square)
    lower_left_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, lower_left_square)
    lower_right_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, lower_right_square)
    # end of identification of squares for each new graph fragment


    upper_right_fragment = GraphFragment(upper_right_fragment_squares, [upper_right_vertice,
                                                        middle_middle_vertice, middle_right_vertice,upper_middle_vertice,
                                                        upper_right_square_middle_vertice], graph_fragment.layer_number + 1, [(middle_middle_vertice.id, upper_middle_vertice.id), (upper_middle_vertice.id, upper_right_vertice.id), (upper_right_vertice.id, middle_right_vertice.id), (middle_right_vertice.id, middle_middle_vertice.id),
                           (middle_middle_vertice.id, upper_right_square_middle_vertice.id), (upper_middle_vertice.id, upper_right_square_middle_vertice.id), (upper_right_vertice.id, upper_right_square_middle_vertice.id), (middle_right_vertice.id, upper_right_square_middle_vertice.id)], upper_right_square_middle_vertice)
    lower_right_fragment = GraphFragment(lower_right_fragment_squares, [lower_right_vertice,
                                                        middle_middle_vertice, middle_right_vertice, lower_middle_vertice, lower_right_square_middle_vertice], graph_fragment.layer_number + 1, [(middle_middle_vertice.id, middle_right_vertice.id), (middle_right_vertice.id, lower_right_vertice.id), (lower_right_vertice.id, lower_middle_vertice.id), (lower_middle_vertice.id, middle_middle_vertice.id), (middle_middle_vertice.id, lower_right_square_middle_vertice.id), (middle_right_vertice.id, lower_right_square_middle_vertice.id), (lower_right_vertice.id, lower_right_square_middle_vertice.id), (lower_middle_vertice.id, lower_right_square_middle_vertice.id)], lower_right_square_middle_vertice)
    upper_left_fragment = GraphFragment(upper_left_fragment_squares, [upper_left_vertice,
                                                        middle_middle_vertice, middle_left_vertice, upper_middle_vertice,
                                                        upper_left_square_middle_vertice], graph_fragment.layer_number + 1, [(middle_middle_vertice.id, middle_left_vertice.id), (middle_left_vertice.id, upper_left_vertice.id), (upper_left_vertice.id, upper_middle_vertice.id), (upper_middle_vertice.id, middle_middle_vertice.id), (middle_middle_vertice.id, upper_left_square_middle_vertice.id), (middle_left_vertice.id, upper_left_square_middle_vertice.id), (upper_left_vertice.id, upper_left_square_middle_vertice.id), (upper_middle_vertice.id, upper_left_square_middle_vertice.id)], upper_left_square_middle_vertice)
    lower_left_fragment = GraphFragment(lower_left_fragment_squares, [lower_left_vertice,
                                                        middle_middle_vertice, middle_left_vertice,
                                                        lower_middle_vertice,lower_left_square_middle_vertice], graph_fragment.layer_number + 1,[(lower_left_vertice.id, middle_left_vertice.id), (middle_left_vertice.id, middle_middle_vertice.id),(middle_middle_vertice.id, lower_middle_vertice.id), (lower_middle_vertice.id, lower_left_vertice.id), (lower_left_vertice.id, lower_left_square_middle_vertice.id), (middle_left_vertice.id, lower_left_square_middle_vertice.id),(lower_middle_vertice.id, lower_left_square_middle_vertice.id), (middle_middle_vertice.id, lower_left_square_middle_vertice.id)], lower_left_square_middle_vertice)


    verticies_graph_fragment.pop(id, None)
    set_labels_in_graph_fragment(upper_right_fragment)

    set_labels_in_graph_fragment(lower_right_fragment)
    set_labels_in_graph_fragment(upper_left_fragment)
    set_labels_in_graph_fragment(lower_left_fragment)

    verticies_graph_fragment[upper_right_fragment.middle_vertex.id] = upper_right_fragment
    verticies_graph_fragment[lower_right_fragment.middle_vertex.id] = lower_right_fragment
    verticies_graph_fragment[upper_left_fragment.middle_vertex.id] = upper_left_fragment
    verticies_graph_fragment[lower_left_fragment.middle_vertex.id] = lower_left_fragment
    graph_fragment_list.append(upper_right_fragment)
    graph_fragment_list.append(lower_right_fragment)
    graph_fragment_list.append(upper_left_fragment)
    graph_fragment_list.append(lower_left_fragment)
    inter_layer_connections.append((upper_right_fragment.middle_vertex.id, id))
    inter_layer_connections.append((lower_right_fragment.middle_vertex.id, id))
    inter_layer_connections.append((upper_left_fragment.middle_vertex.id, id))
    inter_layer_connections.append((lower_left_fragment.middle_vertex.id, id))
    graph_fragment.middle_vertex.label = VertexLabel.i
    sorted_graph_fragment_list = sort_graph_fragments(graph_fragment_list)
    graph_fragment_list.clear()

    graph_fragment_list.extend(sorted_graph_fragment_list)
