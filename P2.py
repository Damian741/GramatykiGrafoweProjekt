import math
from common import *
from VerticeLabel import VerticeLabel

def P2(id):
    graph_fragment = verticies_graph_fragment.get(id)
    lower_layer_squares = resolve_lower_layer_squares(graph_fragment)
    lower_left_vertice = find_lower_left_vertice(lower_layer_squares)
    lower_graph_fragment_width = math.sqrt(len(lower_layer_squares))
    middle_left_vertice_y = lower_left_vertice.y + lower_graph_fragment_width / 2
    upper_left_vertice_y = lower_left_vertice.y + lower_graph_fragment_width
    lower_middle_vertice_x = lower_left_vertice.x + lower_graph_fragment_width / 2
    lower_right_vertice_x = lower_left_vertice.x + lower_graph_fragment_width
    upper_right_square_middle_x = lower_middle_vertice_x + lower_graph_fragment_width / 4
    upper_right_square_middle_y = middle_left_vertice_y + lower_graph_fragment_width / 4
    lower_right_square_middle_y = lower_left_vertice.y + lower_graph_fragment_width / 4
    upper_Left_square_middle_x = lower_left_vertice.x + lower_graph_fragment_width / 4

    lower_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_vertice_x, lower_left_vertice.y, lower_layer_squares)
    upper_left_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_left_vertice.x, upper_left_vertice_y, lower_layer_squares)
    upper_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_vertice_x, upper_left_vertice_y, lower_layer_squares)
    middle_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_middle_vertice_x, middle_left_vertice_y, lower_layer_squares)
    middle_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_vertice_x, middle_left_vertice_y, lower_layer_squares)
    middle_left_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_left_vertice.x, middle_left_vertice_y, lower_layer_squares)
    upper_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_middle_vertice_x, upper_left_vertice_y, lower_layer_squares)
    lower_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_middle_vertice_x, lower_left_vertice.y, lower_layer_squares)

    upper_right_square_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_right_square_middle_x, upper_right_square_middle_y, lower_layer_squares)
    lower_right_square_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_right_square_middle_x, lower_right_square_middle_y, lower_layer_squares)
    upper_left_square_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_Left_square_middle_x, upper_right_square_middle_y, lower_layer_squares)
    lower_left_square_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_Left_square_middle_x, lower_right_square_middle_y, lower_layer_squares)

    upper_left_square = None
    upper_right_square = None
    lower_left_square = None
    lower_right_square = None
    for square in lower_layer_squares:
        if upper_left_square == None or square.field_id < upper_left_square.field_id:
            upper_left_square = square
    layer_size = (2 ** upper_left_square.layer_number)
    for square in lower_layer_squares:
        if upper_right_square == None and square.field_id == upper_left_square.field_id + lower_graph_fragment_width / 2:
            upper_right_square = square
        if lower_left_square == None and square.field_id == upper_left_square.field_id + (lower_graph_fragment_width / 2) * layer_size:
            lower_left_square = square
        if lower_right_square == None and square.field_id == (upper_left_square.field_id + (lower_graph_fragment_width / 2) * layer_size) + lower_graph_fragment_width / 2:
            lower_right_square = square
    upper_left_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, upper_left_square)
    upper_right_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, upper_right_square)
    lower_left_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, lower_left_square)
    lower_right_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, lower_right_square)

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
    verticies_graph_fragment[upper_right_fragment.middle_vertice.id] = upper_right_fragment
    verticies_graph_fragment[lower_right_fragment.middle_vertice.id] = lower_right_fragment
    verticies_graph_fragment[upper_left_fragment.middle_vertice.id] = upper_left_fragment
    verticies_graph_fragment[lower_left_fragment.middle_vertice.id] = lower_left_fragment
    graph_fragment_list.append(upper_right_fragment)
    graph_fragment_list.append(lower_right_fragment)
    graph_fragment_list.append(upper_left_fragment)
    graph_fragment_list.append(lower_left_fragment)
    inter_layer_connections.append((upper_right_fragment.middle_vertice.id, id))
    inter_layer_connections.append((lower_right_fragment.middle_vertice.id, id))
    inter_layer_connections.append((upper_left_fragment.middle_vertice.id, id))
    inter_layer_connections.append((lower_left_fragment.middle_vertice.id, id))
    graph_fragment.middle_vertice.label = VerticeLabel.i