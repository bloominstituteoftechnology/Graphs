#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

import random
from sys import argv
from graph import Graph
from draw import BokehGraph


def main(v=5, e=5):
    graph = Graph()
    for i in range(v):
        graph.add_vertex(i)
    for j in range(e):
        # TODO: Need to check if edge is unique
        rand_vert = int(random.random() * v)
        rand_edge = int(random.random() * e)
        print(rand_vert, rand_edge)
        graph.add_edge(rand_vert, rand_edge)
    print(graph.vertices)
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 3:
        v = argv[1]
        e = argv[2]
        main(int(v), int(e))
    else:
        main()
