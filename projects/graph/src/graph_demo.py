#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

import random
from sys import argv
from graph import Graph
from draw import BokehGraph


def main(v=10, e=5, connected=True):
    graph = Graph()
    for i in range(v):
        graph.add_vertex(i)

    all_edges = []
    for i in range(v):
        for j in range(i+1, v):
            all_edges.append((i, j))

    random.shuffle(all_edges)
    edges = all_edges[:e]

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    graph.connected()
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show(connected)


if __name__ == '__main__':
    if len(argv) == 3:
        v = argv[1]
        e = argv[2]
        main(int(v), int(e))
    else:
        main()
