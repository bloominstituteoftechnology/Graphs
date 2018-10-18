#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(num_vertices=8, num_edges=8, draw_components=True):
    """Build and show random graph."""
    graph = Graph()
    # Add appropriate number of vertices
    for num in range(num_vertices):
        graph.add_vertex(Vertex(label=str(num)))

    # Add random edges between vertices
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        # TODO check if edge already exists
        graph.add_edge(vertices[0], vertices[1])

    bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
    else:
        print('Expected arguments: num_vertices num_edges draw_components')
        print('Both numbers should be integers, draw_components should be 0/1')
















# #!/usr/bin/python

# """
# Demonstration of Graph and BokehGraph functionality.
# """
# from random import sample
# from sys import argv
# from graph import Vertex, Graph
# from draw import BokehGraph

# def main(num_vertices, num_edges, draw_components=True):
#     graph = Graph()
#     for num in range(num_vertices):
#         graph.add_vertex(num)

#     for _ in range(num_edges):
#         vertex1 = sample(graph.vertices.keys(), 1)[0]
#         vertex2 = sample(graph.vertices.keys(), 1)[0]
#         graph.add_edge(vertex1, vertex2)

#     bokeh_graph = BokehGraph(graph, draw_components=draw_components)
#     bokeh_graph.draw()

# if __name__ == '__main__':
#     if len(argv) == 4:
#         NUM_VERTICES = int(argv[1])
#         NUM_EDGES = int(argv[2])
#         DRAW_COMPONENTS = bool(int(argv[3]))
#         main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
#     else:
#         print('Expected arguments: num_verts num_edges draw_components ')
#         print('Both numbers should be integers, draw_components should be 0/1')
























