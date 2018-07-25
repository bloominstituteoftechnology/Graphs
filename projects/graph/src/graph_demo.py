#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from random import sample
from draw import BokehGraph
from graph import Graph

def main(verts=8, edges=8):
    graph = Graph()
    for verts in range(verts):
        graph.create_vertex(str(verts))

    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        graph.create_edge(vertices[0], vertices[1])

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()

if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()