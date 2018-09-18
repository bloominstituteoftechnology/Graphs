#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph


def main():
    # create graph
    graph = Graph()

    # Add vertexes
    graph.add_vertex('v1')
    graph.add_vertex('v2')
    graph.add_vertex('v3')
    graph.add_vertex('v4')
    graph.add_vertex('v5')
    graph.add_vertex('v6')

    # add edges
    graph.add_edge('v1', 'v2')
    graph.add_edge('v2', 'v1')
    graph.add_edge('v2', 'v6')
    graph.add_edge('v3', 'v5')
    graph.add_edge('v5', 'v6')
    graph.add_edge('v5', 'v6')
    graph.add_edge('v6', 'v5')

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    # TODO - parse argv
    main()
