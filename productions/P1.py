from common import *
from data.VertexLabel import VertexLabel
from util.SortUtils import sort_graph_fragments


def P1(id):
    global verticies_graph_fragment
    global graph_fragment_list
    graph_fragment = verticies_graph_fragment.get(id)  # check if a graph fragment is registered as possible to extend to lower layers
    lower_layer_squares = resolve_lower_layer_squares(graph_fragment)  # get squares which a new fragment on lower level will occupy
    lower_left_vertice = find_lower_left_vertice(lower_layer_squares)  # find the edge lowest vertice on the left
    lower_graph_fragment_width = math.sqrt(len(lower_layer_squares))  # length of a whole square (consisting of small squares) which the new graph fragment occupies
    lower_right_x = lower_left_vertice.x + lower_graph_fragment_width  # define new graph fragment vertices coordinates
    lower_right_y = lower_left_vertice.y
    upper_left_x = lower_left_vertice.x
    upper_left_y = lower_left_vertice.y + lower_graph_fragment_width
    upper_right_x = lower_right_x
    upper_right_y = upper_left_y
    middle_x = lower_left_vertice.x + (lower_graph_fragment_width / 2)
    middle_y = lower_left_vertice.y + (lower_graph_fragment_width / 2)
    lower_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(lower_right_x, lower_right_y, # define vertices and remove duplicate vertices for neighbouring squares
                                                                              lower_layer_squares)
    upper_left_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_left_x, upper_left_y,
                                                                             lower_layer_squares)
    upper_right_vertice = find_vertice_with_coordinates_and_remove_duplicates(upper_right_x, upper_right_y,
                                                                              lower_layer_squares)
    middle_vertice = find_vertice_with_coordinates_and_remove_duplicates(middle_x, middle_y, lower_layer_squares)

    edges = [(upper_left_vertice.id, lower_left_vertice.id), (upper_left_vertice.id, upper_right_vertice.id),   # define edges (connections between vertices (their ids))
             (upper_left_vertice.id, middle_vertice.id),
             (lower_left_vertice.id, lower_right_vertice.id), (lower_left_vertice.id, middle_vertice.id),
             (lower_right_vertice.id, middle_vertice.id),
             (lower_right_vertice.id, upper_right_vertice.id), (upper_right_vertice.id, middle_vertice.id)]
    new_fragment = GraphFragment(lower_layer_squares,   # define new graph fragment on lower layer
                                 [lower_left_vertice, lower_right_vertice, upper_left_vertice, upper_right_vertice,
                                  middle_vertice], graph_fragment.layer_number + 1, edges,
                                 middle_vertice)
    verticies_graph_fragment.pop(id, None)  # remove old fragment (the one from which we were generating the lower one) from the list of registered graph fragments to generate something from it
    verticies_graph_fragment[middle_vertice.id] = new_fragment  # register the new lower fragment as a one from which you can generate something
    graph_fragment_list.append(new_fragment)  # add fragment to a graph list
    inter_layer_connections.append((middle_vertice.id, id))  # create connection between graph fragments (also between layers)
    set_labels_in_graph_fragment(new_fragment)
    graph_fragment.middle_vertice.label = VertexLabel.i  # set upper graph fragment middle vertice label to i - occupied
    sorted_graph_fragment_list = sort_graph_fragments(graph_fragment_list)
    graph_fragment_list.clear()
    graph_fragment_list.extend(sorted_graph_fragment_list)  # update graph_fragment_list to sorted one
