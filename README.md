# Projekt Siatka Czworokątna 1

## 1. Graph generation
To generate a graph visually you need to define which productions you want to use on which vertices in main.py.
The first vertice has id = 0. The rest you need to specify by invoking the program and checking generated graph ids.

## 2. Iterating over the graph
To create a loop which generates the graph you need to use graph_fragment_list - a list which
contains all graph fragments sorted by:
1. Layer level
2. Y coordinate (reversed as the graph goes down from 0 to -infinity)
3. X coordinate

You can obtain graph fragments from that list - each graph fragment has middle_vertice which has
id. This id should be applied to a production.

## 3. What should each production do?

1. Get graph fragments for the left side of production (graph_fragment_list list or vertices_graph_fragment dictionary from common.py)
2. (a) Get lower layer squares which will be occupied by new fragment (resolve_lower_layer_squares from common.py)
3. (a) Find vertices to be used in production in squares collection - coordinates resolution custom for each production, then having coordinates use find_vertice_with_coordinates_and_remove_duplicates from common.py to get your vertices (b) Modify the existing vertices in graph fragments
4. Define edges
5. (a) Define new fragment or (b) Update existing graph fragments
6. Update collections representing the graph (label edges, update graph fragments, sort graph fragments etc. - details in P1 comments)

a - productions generating something on lower layers <br>
b - productions merging existing graph fragments

