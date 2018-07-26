#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""


from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(num_vertices=8, num_edges=8):
    """Build and show random graph."""
    graph = Graph()

    graph.random_graph(num_vertices, num_edges)
    graph.get_connected_components()
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()
    # print(graph.vertices['0'].color)



if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()  # accept defaults