from GraphFragment import GraphFragment
from Square import Square
import math
from Vertice import Vertice
import networkx as nx
import matplotlib.pyplot as plt


BETWEEN_LAYER_BUFFER = 5 #to change
verticies_graph_fragment = { 0 : GraphFragment([], [Vertice(0, 0, 0)], -1, [], Vertice(0, 0, 0)) }
graph_fragment_list = [GraphFragment([], [Vertice(0, 0, 0)], -1, [], Vertice(0, 0, 0))]
inter_layer_connections = []
graph_verticies_id_counter = 1

def resolve_row_for_square(square):
    divider = 2**square.layer_number
    return square.field_id // divider

def resolve_column_for_square(square):
    divider = 2**square.layer_number
    return square.field_id % divider

def resolve_upper_left_lower_layer_square_id(square_row, square_column, square):
    return square_row * (2**(square.layer_number + 2)) + (square_column * 2)

def resolve_lower_left_lower_layer_square_id(square_row, square_column, square):
    return (square_row * (2**(square.layer_number + 2)) + (square_column * 2)) + (2**(square.layer_number + 1))

def append_generated_lower_layer_squares(square, lower_layer_squares):
    lower_square_layer = square.layer_number + 1
    square_row = resolve_row_for_square(square)
    square_column = resolve_column_for_square(square)
    upper_left_lower_layer_square_id = resolve_upper_left_lower_layer_square_id(square_row, square_column, square)
    upper_right_lower_layer_square_id = upper_left_lower_layer_square_id + 1
    lower_left_lower_layer_square_id = resolve_lower_left_lower_layer_square_id(square_row, square_column, square)
    lower_right_lower_layer_square_id = lower_left_lower_layer_square_id + 1
    lower_layer_squares.append(Square(upper_left_lower_layer_square_id, lower_square_layer))
    lower_layer_squares.append(Square(upper_right_lower_layer_square_id, lower_square_layer))
    lower_layer_squares.append(Square(lower_left_lower_layer_square_id, lower_square_layer))
    lower_layer_squares.append(Square(lower_right_lower_layer_square_id, lower_square_layer))

def resolve_verticies_coordinates_for_square(square):
    global graph_verticies_id_counter
    square_layer = square.layer_number
    acc = -BETWEEN_LAYER_BUFFER
    for i in range(square_layer):
        layer_size = (2 ** i)
        acc -= (layer_size + BETWEEN_LAYER_BUFFER)
    breaks = 0
    if square_layer > 2:
        for i in range(2, square_layer):
            layer_size = (2 ** (i - 1))
            breaks = layer_size - 1
    acc -= breaks
    square_row = resolve_row_for_square(square)
    square_column = resolve_column_for_square(square)
    y_upper_left_vertice = acc - square_row - (square_row // 2)
    x_upper_left_vertice = square_column + (square_column // 2)
    square.verticies.append(Vertice(x_upper_left_vertice, y_upper_left_vertice, graph_verticies_id_counter))
    graph_verticies_id_counter += 1
    square.verticies.append(Vertice(x_upper_left_vertice + 1, y_upper_left_vertice, graph_verticies_id_counter))
    graph_verticies_id_counter += 1
    square.verticies.append(Vertice(x_upper_left_vertice, y_upper_left_vertice - 1, graph_verticies_id_counter))
    graph_verticies_id_counter += 1
    square.verticies.append(Vertice(x_upper_left_vertice + 1, y_upper_left_vertice - 1, graph_verticies_id_counter))
    graph_verticies_id_counter += 1
    square.verticies.append(Vertice(x_upper_left_vertice + 0.5, y_upper_left_vertice - 0.5, graph_verticies_id_counter))
    graph_verticies_id_counter += 1

def resolve_lower_layer_squares(graph_fragment):
    squares_list = graph_fragment.squares
    lower_layer_squares = []
    if len(squares_list) == 0:
        lower_layer_squares.append(Square(0, 0))
        resolve_verticies_coordinates_for_square(lower_layer_squares[0])
        return lower_layer_squares
    for square in squares_list:
        append_generated_lower_layer_squares(square, lower_layer_squares)
    for square in lower_layer_squares:
        resolve_verticies_coordinates_for_square(square)
    return lower_layer_squares

def find_lower_left_vertice(lower_layer_squares):
    min_square_vertice = None
    for square in lower_layer_squares:
        for vertice in square.verticies:
            if min_square_vertice is None or min_square_vertice.x > vertice.x or min_square_vertice.y > vertice.y:
                min_square_vertice = vertice
    return min_square_vertice

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
    new_fragment = GraphFragment(lower_layer_squares, [lower_left_vertice, lower_right_vertice, upper_left_vertice, upper_right_vertice, middle_vertice], graph_fragment.layer_number + 1, edges, [middle_vertice])
    verticies_graph_fragment.pop(id, None)
    verticies_graph_fragment[middle_vertice.id] = new_fragment
    graph_fragment_list.append(new_fragment)
    inter_layer_connections.append((middle_vertice.id, id))

P1(0)
P2(5)
G = nx.Graph()
for graph_fragment in graph_fragment_list:
    for vertice in graph_fragment.verticies:
        G.add_node(vertice.id)
for graph_fragment in graph_fragment_list:
    for edge in graph_fragment.edges:
        G.add_edge(edge[0], edge[1])
for inter_layer_connection in inter_layer_connections:
    G.add_edge(inter_layer_connection[0], inter_layer_connection[1])
pos = {}
for graph_fragment in graph_fragment_list:
    for vertice in graph_fragment.verticies:
        pos[vertice.id] = (vertice.x, vertice.y)
nx.draw_networkx(G, pos, node_color='lightblue')#, node_size = 10, font_size=1)
ax = plt.gca()
plt.axis("off")
plt.show()