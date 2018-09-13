#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random


def main(vertices, edges):
    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(6, 8)

    bokeh_graph = BokehGraph(graph)

    bokeh_graph.draw()


if __name__ == '__main__':
    # TODO - parse argv
    main()
