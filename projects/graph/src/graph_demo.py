#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
import random
from graph import Graph
from draw import BokehGraph


def main(v=6, e=6):
    graph = Graph()
    for i in range(v):
        graph.add_vertex(i)
    for j in range(e):
        random_vertex = int(random.random() * v)
        random_edge = int(random.random() * e)
        print(random_vertex, random_edge)
        graph.add_edge(random_vertex, random_edge)
    bg = BokehGraph(graph)
    bg.draw()

    # if num_vertices is None:
    #     num_vertices = random.randint(3,9)
    # else:
    #     num_vertices = int(num_vertices)
    # if num_edges is None:
    #     num_edges = random.randint(num_vertices * (num_vertices - 1) / 2)


if __name__ == '__main__':
    if len(argv) == 3:
        v = argv[1]
        e = argv[2]
        main(int(v), int(e))
    else:
        main()
