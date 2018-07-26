#!/usr/bin/env python

"""
Demo of Graph and BokehGraph
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(num_vertices=6, num_edges=6, draw_comps=True):
    """Build and show random graph."""
    graph = Graph()
    for num in range(num_vertices):
        graph.add_vertex(Vertex(label=str(num)))

    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        graph.add_edge(vertices[0], vertices[1])

    bokeh_graph = BokehGraph(graph, draw_comps=draw_comps)
    bokeh_graph.show()


if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPS = bool(int(argv[3]))
        main(NUM_VERTICES, NUM_EDGES, DRAW_COMPS)
    else:
        print('Expected arguments: num_vertices num_edges draw_components')
        print('Both numbers should be integers, draw_components should be 0/1')