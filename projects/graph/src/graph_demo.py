#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
from random import choice


def main(height=25, width=25, nodes=6, connections=0):
    new_graph = Graph(height, width)
    for x in range(nodes):
        new_graph.add_vertex(x)
    for _ in range(connections):
        node_1 = choice(list(new_graph.vertices.keys()))
        node_2 = choice(list(new_graph.vertices.keys()))
        if node_1 is not node_2:
            new_graph.add_edge(node_1, node_2)
    bokeh = BokehGraph(new_graph, height, width)
    bokeh.make_graph()


if __name__ == '__main__':
    if len(argv) > 1:
        height = int(argv[1])
        width = int(argv[2])
        nodes = int(argv[3])
        conn_attempts = int(argv[4])
        main(height, width, nodes, conn_attempts)
    else:
        print('Using defaults...')
        main()
