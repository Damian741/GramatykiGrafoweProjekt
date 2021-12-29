import math
from data.Square import Square
from data.Vertice import Vertice
from data.GraphFragment import GraphFragment
from data.VerticeLabel import VerticeLabel

"""
_BETWEEN_LAYER_BUFFER - constant value which defines space between given graph layers
_graph_verticies_id_counter - verticies counter which assigns ID to each vertice
_start_vertice - first vertice of the graph
_start_fragment - first fragment of the graph
verticies_graph_fragment - list of all verticies which allows you to generate graph fragments on the lower layer
graph_fragment_list - list of all graph fragments generated by productions
inter_layer_connections - list of all connections between upper and lower layers
"""
_BETWEEN_LAYER_BUFFER = 1  # possible to modify
_graph_verticies_id_counter = 1
_start_vertice = Vertice(0, 0, 0, VerticeLabel.I)
_start_fragment = GraphFragment([], [_start_vertice], -1, [], _start_vertice)
verticies_graph_fragment = {0: _start_fragment}
graph_fragment_list = [_start_fragment]
inter_layer_connections = []

"""
Function which returns row for given single square
"""
def _resolve_row_for_square(square):
    divider = 2 ** square.layer_number
    return square.field_id // divider


"""
Function which returns column for given single square
"""
def _resolve_column_for_square(square):
    divider = 2 ** square.layer_number
    return square.field_id % divider


"""
Function which returns ID of upper left square on the lower layer 
"""
def _resolve_upper_left_lower_layer_square_id(square_row, square_column, square):
    return square_row * (2 ** (square.layer_number + 2)) + (square_column * 2)

"""
Function which returns ID of lower left square on the lower layer 
"""
def _resolve_lower_left_lower_layer_square_id(square_row, square_column, square):
    return (square_row * (2 ** (square.layer_number + 2)) + (square_column * 2)) + (2 ** (square.layer_number + 1))

"""
Function which generates 4 squares on lower layer for each square from upper layer 
and appends these 4 squares to lower_layer_squares list
"""
def _append_generated_lower_layer_squares(square, lower_layer_squares):
    lower_square_layer = square.layer_number + 1
    square_row = _resolve_row_for_square(square)
    square_column = _resolve_column_for_square(square)
    upper_left_lower_layer_square_id = _resolve_upper_left_lower_layer_square_id(square_row, square_column, square)
    upper_right_lower_layer_square_id = upper_left_lower_layer_square_id + 1
    lower_left_lower_layer_square_id = _resolve_lower_left_lower_layer_square_id(square_row, square_column, square)
    lower_right_lower_layer_square_id = lower_left_lower_layer_square_id + 1
    lower_layer_squares.append(Square(upper_left_lower_layer_square_id, lower_square_layer))
    lower_layer_squares.append(Square(upper_right_lower_layer_square_id, lower_square_layer))
    lower_layer_squares.append(Square(lower_left_lower_layer_square_id, lower_square_layer))
    lower_layer_squares.append(Square(lower_right_lower_layer_square_id, lower_square_layer))

"""
Function which returns coordinates for all vertices of a single square 
"""
def _resolve_verticies_coordinates_for_square(square):
    global _graph_verticies_id_counter
    square_layer = square.layer_number
    acc = -_BETWEEN_LAYER_BUFFER
    for i in range(square_layer):
        layer_size = (2 ** i)
        acc -= (layer_size + _BETWEEN_LAYER_BUFFER)
    breaks = 0
    if square_layer > 2:
        for i in range(2, square_layer):
            layer_size = (2 ** (i - 1))
            breaks = layer_size - 1
    acc -= breaks
    square_row = _resolve_row_for_square(square)
    square_column = _resolve_column_for_square(square)
    y_upper_left_vertice = acc - square_row - (square_row // 2)
    x_upper_left_vertice = square_column + (square_column // 2)
    square.verticies.append(
        Vertice(x_upper_left_vertice, y_upper_left_vertice, _graph_verticies_id_counter, VerticeLabel.UNDEFINED))
    _graph_verticies_id_counter += 1
    square.verticies.append(
        Vertice(x_upper_left_vertice + 1, y_upper_left_vertice, _graph_verticies_id_counter, VerticeLabel.UNDEFINED))
    _graph_verticies_id_counter += 1
    square.verticies.append(
        Vertice(x_upper_left_vertice, y_upper_left_vertice - 1, _graph_verticies_id_counter, VerticeLabel.UNDEFINED))
    _graph_verticies_id_counter += 1
    square.verticies.append(Vertice(x_upper_left_vertice + 1, y_upper_left_vertice - 1, _graph_verticies_id_counter,
                                    VerticeLabel.UNDEFINED))
    _graph_verticies_id_counter += 1
    square.verticies.append(Vertice(x_upper_left_vertice + 0.5, y_upper_left_vertice - 0.5, _graph_verticies_id_counter,
                                    VerticeLabel.UNDEFINED))
    _graph_verticies_id_counter += 1

"""
Function which returns all single squares for all graph fragments generated on the right side of the production
"""
def resolve_lower_layer_squares(graph_fragment):
    squares_list = graph_fragment.squares
    lower_layer_squares = []
    if len(squares_list) == 0:
        lower_layer_squares.append(Square(0, 0))
        _resolve_verticies_coordinates_for_square(lower_layer_squares[0])
        return lower_layer_squares
    for square in squares_list:
        _append_generated_lower_layer_squares(square, lower_layer_squares)
    for square in lower_layer_squares:
        _resolve_verticies_coordinates_for_square(square)
    return lower_layer_squares

"""
Function which returns lower left vertice from lower_layer_squares list
"""
def find_lower_left_vertice(lower_layer_squares):
    min_square_vertice = None
    for square in lower_layer_squares:
        for vertice in square.verticies:
            if min_square_vertice is None or min_square_vertice.x > vertice.x or min_square_vertice.y > vertice.y:
                min_square_vertice = vertice
    return min_square_vertice

"""
Function which returns a vertice for coordinates and removes 
its duplicates (other objects representing vertice with the same coords) from neighbouring squares
"""
def find_vertice_with_coordinates_and_remove_duplicates(x, y, lower_layer_squares):
    result_vertice = None
    verticies_to_delete = []
    for square in lower_layer_squares:
        for vertice in square.verticies:
            if vertice.x == x and vertice.y == y:
                if result_vertice is None:
                    result_vertice = vertice
                else:
                    verticies_to_delete.append(vertice)
    for vertice_to_delete in verticies_to_delete:
        for square in lower_layer_squares:
            if vertice_to_delete in square.verticies:
                square.verticies.remove(vertice_to_delete)
                square.verticies.append(result_vertice)
    return result_vertice

"""
Function which returns all single squares located in upper left square
"""
def return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, upper_left_square):
    result_squares = []
    upper_left_square_column = _resolve_column_for_square(upper_left_square)
    upper_left_square_row = _resolve_row_for_square(upper_left_square)
    lower_layer_width = math.sqrt(len(lower_layer_squares)) / 2
    for square in lower_layer_squares:
        if (_resolve_row_for_square(square) >= upper_left_square_row and _resolve_row_for_square(
                square) < upper_left_square_row + lower_layer_width and upper_left_square_column <= _resolve_column_for_square(
            square) < upper_left_square_column + lower_layer_width):
            result_squares.append(square)
    return result_squares

"""
Function which sets labels in graph fragment
"""
def set_labels_in_graph_fragment(graph_fragment):
    for vertice in graph_fragment.verticies:
        vertice.label = VerticeLabel.E
    graph_fragment.middle_vertice.label = VerticeLabel.I