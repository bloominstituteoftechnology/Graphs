#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
import random
import math
from graph import Graph
from draw import BokehGraph

def main(v, e):
    graph = Graph()
    for vertex in range(v):
        graph.add_vertex(vertex)
    edges = []
    for i in range(v):
        for j in range(v):
            if i < j:
                edges.append((i,j))
    random.shuffle(edges)
    randomEdges = edges[:e]
    print(randomEdges)
    for edge in randomEdges:
        graph.add_edge(edge[0], edge[1])
    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    # TODO - parse argv
    main(10,5)
