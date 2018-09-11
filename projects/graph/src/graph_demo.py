#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from draw import BokehGraph
from graph import Graph
from random import sample

def main(vert_args=5, edge_args=5):
    g = Graph()

    for vertex in range(vert_args):
        g.add_vertex(str(vertex))

    for edge in range(edge_args):
        vertices = sample(g.vertices.keys(), 2)
        g.add_edge(vertices[0], vertices[1])

    b = BokehGraph(g)
    b.setup_graph()
    b.show_plot()

if __name__ == '__main__':
    if len(argv) >= 3:
        vert_args = int(argv[1])
        edge_args = int(argv[2])
        main(vert_args, edge_args)
    else:
        print('Expected args: vert_args, edge_args')
