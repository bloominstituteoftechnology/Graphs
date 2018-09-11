#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
from random import randint

def main(vertices=6, edges=4):
    graph = Graph()

    for v in range(vertices):
        graph.add_vertex(v)

    for _ in range(edges):
        vertex = [randint(0, vertices - 1), randint(0, vertices - 1)]
        graph.add_edge(vertex[0], vertex[1])

    BokehGraph(graph).show()

if __name__ == '__main__':
    # TODO - parse argv
    if len(argv) > 2:
        vertices = int(argv[1])
        edges = int(argv[2])
        main(vertices, edges)
    else:
        main()
