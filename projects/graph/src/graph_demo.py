#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph


def main(vertices = 4, edge_prob=0.5, layout = 'circle', colors='orange', output=None):
    graph = Graph(vertices, edge_prob)
    graph.generate_vertices()
    graph.generate_edges()

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()

if __name__ == '__main__':
    # TODO - parse argv
    main(*argv[1:])
