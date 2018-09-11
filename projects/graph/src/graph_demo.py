#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from random import sample
from draw import BokehGraph
from graph import Graph


def main(num_vertices=0, num_edges=0, draw_components=True):
    graph = Graph()
    for number in range(num_vertices):
        graph.add_vertex()

    for _ in range(num_edges):
        verticles = sample(graph.vertices.keys(), 2)
        graph.add_edge(vertices[0], vertices[1])

    bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    bokeh_graph.show()


if __name__ == '__main__':
    # TODO - parse argv
    main()
