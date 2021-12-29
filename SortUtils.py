def sort_graph_fragments(graph_fragment_list):
    graph_fragment_list = _sort_by_level(graph_fragment_list)
    graph_fragment_list = _sort_by_y(graph_fragment_list)
    graph_fragment_list = _sort_by_x(graph_fragment_list)
    return graph_fragment_list


def _sort_by_level(graph_fragment_list):
    graph_fragment_list.sort(key=lambda x: x.layer_number)
    return graph_fragment_list



def _sort_by_y(graph_fragment_list):
    sorted_graph_fragment_list = []
    graph_fragment_list_length = len(graph_fragment_list)
    first_fragment_in_level = graph_fragment_list[0]
    graph_fragments_same_level = [first_fragment_in_level]
    for i in range(1, graph_fragment_list_length):
        if graph_fragment_list[i].layer_number == first_fragment_in_level.layer_number:
            graph_fragments_same_level.append(graph_fragment_list[i])
            continue
        graph_fragments_same_level.sort(key=lambda x: x.middle_vertice.y, reverse=True)
        sorted_graph_fragment_list.extend(graph_fragments_same_level)
        first_fragment_in_level = graph_fragment_list[i]
        graph_fragments_same_level = [first_fragment_in_level]
    graph_fragments_same_level.sort(key=lambda x: x.middle_vertice.y, reverse=True)
    sorted_graph_fragment_list.extend(graph_fragments_same_level)
    return sorted_graph_fragment_list

def _sort_by_x(graph_fragment_list):
    sorted_graph_fragment_list = []
    graph_fragment_list_length = len(graph_fragment_list)
    first_fragment_in_y = graph_fragment_list[0]
    graph_fragments_same_y = [first_fragment_in_y]
    for i in range(1, graph_fragment_list_length):
        if graph_fragment_list[i].middle_vertice.y == first_fragment_in_y.middle_vertice.y:
            graph_fragments_same_y.append(graph_fragment_list[i])
            continue
        graph_fragments_same_y.sort(key=lambda x: x.middle_vertice.x)
        sorted_graph_fragment_list.extend(graph_fragments_same_y)
        first_fragment_in_y = graph_fragment_list[i]
        graph_fragments_same_y = [first_fragment_in_y]
    graph_fragments_same_y.sort(key=lambda x: x.middle_vertice.x)
    sorted_graph_fragment_list.extend(graph_fragments_same_y)
    return sorted_graph_fragment_list