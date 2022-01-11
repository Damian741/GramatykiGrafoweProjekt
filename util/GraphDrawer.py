import networkx as nx
import matplotlib.pyplot as plt
from common import graph_fragment_list, inter_layer_connections
from data.VertexLabel import VertexLabel

label_color_map = {
    VertexLabel.E: 'blue',
    VertexLabel.I: 'orange',
    VertexLabel.i: 'red'
}
color_list = []

"""
Function for drawing graphs
"""


def draw_graph():
    global color_list
    G = nx.Graph()
    for graph_fragment in graph_fragment_list:
        for vertice in graph_fragment.vertices:
            if G.nodes.get(vertice.id) is None:
                G.add_node(vertice.id)
                color_list.append(label_color_map[vertice.label])
    for graph_fragment in graph_fragment_list:
        for edge in graph_fragment.edges:
            G.add_edge(edge[0], edge[1])
    for inter_layer_connection in inter_layer_connections:
        G.add_edge(inter_layer_connection[0], inter_layer_connection[1])
    pos = {}
    for graph_fragment in graph_fragment_list:
        for vertice in graph_fragment.vertices:
            pos[vertice.id] = (vertice.x, vertice.y)
    nx.draw_networkx(G, pos, node_color=color_list)  # , node_size = 10, font_size=1)
    ax = plt.gca()
    plt.axis("off")
    plt.show()
