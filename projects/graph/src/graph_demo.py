#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from random import sample
from draw import BokehGraph
from graph import Graph


def main(vertices=10, edges=10):
    '''Build a random Graph'''
    graph = Graph()
    for num in range(vertices):
        graph.add_vertex(num)

    for _ in range(edges):
        vertices = sample(graph.vertices.keys(), 2)
        graph.add_edge(vertices[0], vertices[1])

    bokeh_graph = BokehGraph(graph, title="Random Graph")
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 3:
        VERTICES = int(argv[1])
        EDGES = int(argv[2])
        if EDGES > (VERTICES * (VERTICES - 1))/2:
            print('Too many edges. Choose a lower number')
        else:
            main(VERTICES, EDGES)
    else:
        print('Expected arguments: Vertices(int) Edges(int)')
