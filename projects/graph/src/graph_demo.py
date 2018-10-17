#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

import random
from sys import argv
from graph import Graph
from draw import BokehGraph


def main(v=10, e=5):
    graph = Graph()
    for i in range(v):
        graph.add_vertex(i)

    all_edges = []
    for i in range(e):
        for j in range(i+1, e):
            all_edges.append((i, j))

    random.shuffle(all_edges)
    edges = all_edges[:e]

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    print(graph.connected())
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show(True)


if __name__ == '__main__':
    if len(argv) == 3:
        v = argv[1]
        e = argv[2]
        main(int(v), int(e))
    else:
        main()
