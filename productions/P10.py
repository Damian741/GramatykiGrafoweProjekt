from common import *
from data.VertexLabel import VertexLabel
from util.SortUtils import sort_graph_fragments

def P10(id):
    global verticies_graph_fragment
    global graph_fragment_list
    graph_fragment = verticies_graph_fragment.get(id) # check if a graph fragment is registered as possible to extend to lower layers
    lower_layer_squares = resolve_lower_layer_squares(graph_fragment) # get squares which a new fragment on lower level will occupy
    
    lower_left_vertice = find_lower_left_vertice(lower_layer_squares) # find the edge lowest vertice on the left
    
    lower_graph_fragment_width = math.sqrt(len(lower_layer_squares)) # length of a whole square (consisting of small squares) which the new graph fragment occupies
    middle_left_vertice_y = lower_left_vertice.y + lower_graph_fragment_width / 2
    upper_left_vertice_y = lower_left_vertice.y + lower_graph_fragment_width
    lower_middle_vertice_x = lower_left_vertice.x + lower_graph_fragment_width / 2
    lower_right_vertice_x = lower_left_vertice.x + lower_graph_fragment_width

    lower_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_vertice_x, lower_left_vertice.y, lower_layer_squares) # define new graph fragment vertices coordinates
    upper_left_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_left_vertice.x, upper_left_vertice_y, lower_layer_squares)
    upper_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_vertice_x, upper_left_vertice_y, lower_layer_squares)
    middle_middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_middle_vertice_x, middle_left_vertice_y, lower_layer_squares)

    square = Square(middle_middle_vertice.id, lower_layer_squares[0].layer_number)
    square.vertices.append([upper_right_vertice, lower_left_vertice, lower_right_vertice, upper_left_vertice, middle_middle_vertice])
    upper_right_fragment = GraphFragment(
        square, 
        [upper_right_vertice, lower_left_vertice, lower_right_vertice, upper_left_vertice, middle_middle_vertice],
         graph_fragment.layer_number + 1, 
         [(middle_middle_vertice.id, upper_right_vertice.id), (middle_middle_vertice.id, lower_left_vertice.id), (middle_middle_vertice.id, lower_right_vertice.id), (middle_middle_vertice.id, upper_left_vertice.id), 
         (lower_left_vertice.id, lower_right_vertice.id), (upper_right_vertice.id, lower_right_vertice.id), (upper_right_vertice.id, upper_left_vertice.id), (lower_left_vertice.id, upper_left_vertice.id)],
         middle_middle_vertice
    )

    verticies_graph_fragment.pop(id, None)
    set_labels_in_graph_fragment(upper_right_fragment)

    verticies_graph_fragment[upper_right_fragment.middle_vertex.id] = upper_right_fragment

    graph_fragment_list.append(upper_right_fragment)

    inter_layer_connections.append((upper_right_fragment.middle_vertex.id, id))

    graph_fragment.middle_vertex.label = VertexLabel.i
    sorted_graph_fragment_list = sort_graph_fragments(graph_fragment_list)
    graph_fragment_list.clear()
    graph_fragment_list.extend(sorted_graph_fragment_list)
