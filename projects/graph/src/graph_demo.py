import random
from sys import argv
from graph import Graph
from draw import BokehGraph

# !/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""


def main(v=7, e=7):
    graph = Graph()
    for i in range(v):
        graph.add_vertex(i)
    for j in range(e):
        random_vertex = int(random.random() * v)
        random_edge = int(random.random() * e)
        graph.add_edge(random_vertex, random_edge)
    bg = BokehGraph(graph)
    bg.draw()
    print(graph.vertices)


if __name__ == '__main__':
    if len(argv) == 3:
        v = argv[1]
        e = argv[2]
        main(int(v).int(e))
    else:
        main()
