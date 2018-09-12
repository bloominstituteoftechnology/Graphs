#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random

from sys import argv
from graph import Graph
from draw import BokehGraph


def main(vertices=6, edges=4):
    graph = Graph()

    for v in range(vertices):
        graph.add_vertex(v)

    all_edges = []

    for i in range(0, vertices):
        for j in range(0, vertices):
            if i < j:
                all_edges.append( (i, j) )

    random.shuffle(all_edges)
    random_edges = all_edges[:edges]

    for edge in random_edges:
        graph.add_edge(edge[0], edge[1])
  
    BokehGraph(graph).show()

if __name__ == '__main__':
    # TODO - parse argv
    if len(argv) > 2:
        vertices = int(argv[1])
        edges = int(argv[2])
        main(vertices, edges)
    else:
        main()
