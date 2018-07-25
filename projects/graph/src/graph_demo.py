#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from draw import BokehGraph
from graph import Graph


def main(num_vertices=None, num_edges=None):
    """Build and show random graph."""
    graph = Graph()
    graph.add_random_data(num_vertices, num_edges)

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()
    print('MAIN CONNECTED COMPONENTS', graph.connected_components)


if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()  # accept defaults
