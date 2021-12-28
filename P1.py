import math
from common import *
from VerticeLabel import VerticeLabel

def P1(id):
    graph_fragment = verticies_graph_fragment.get(id)
    lower_layer_squares = resolve_lower_layer_squares(graph_fragment)
    lower_left_vertice = find_lower_left_vertice(lower_layer_squares)
    lower_graph_fragment_width = math.sqrt(len(lower_layer_squares))
    lower_right_x = lower_left_vertice.x + lower_graph_fragment_width
    lower_right_y = lower_left_vertice.y
    upper_left_x = lower_left_vertice.x
    upper_left_y = lower_left_vertice.y + lower_graph_fragment_width
    upper_right_x = lower_right_x
    upper_right_y = upper_left_y
    middle_x = lower_left_vertice.x + (lower_graph_fragment_width / 2)
    middle_y = lower_left_vertice.y + (lower_graph_fragment_width / 2)
    lower_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_x, lower_right_y,
                                                                              lower_layer_squares)
    upper_left_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_left_x, upper_left_y,
                                                                             lower_layer_squares)
    upper_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_right_x, upper_right_y,
                                                                              lower_layer_squares)
    middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(middle_x, middle_y, lower_layer_squares)

    edges = [(upper_left_vertice.id, lower_left_vertice.id), (upper_left_vertice.id, upper_right_vertice.id), (upper_left_vertice.id, middle_vertice.id),
     (lower_left_vertice.id, lower_right_vertice.id), (lower_left_vertice.id, middle_vertice.id), (lower_right_vertice.id, middle_vertice.id),
     (lower_right_vertice.id, upper_right_vertice.id), (upper_right_vertice.id, middle_vertice.id)]
    new_fragment = GraphFragment(lower_layer_squares, [lower_left_vertice, lower_right_vertice, upper_left_vertice, upper_right_vertice, middle_vertice], graph_fragment.layer_number + 1, edges, middle_vertice)
    verticies_graph_fragment.pop(id, None)
    verticies_graph_fragment[middle_vertice.id] = new_fragment
    graph_fragment_list.append(new_fragment)
    inter_layer_connections.append((middle_vertice.id, id))
    set_labels_in_graph_fragment(new_fragment)
    graph_fragment.middle_vertice.label = VerticeLabel.i
