#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from random import randint
from sys import argv
from draw import BokehGraph
from graph import Graph


def main(vertices, edges):
    """
    Build a random graph and display in browser
    """
    graph = Graph()
    edges_added = []

    for i in range(vertices):
        graph.add_vertex('V{}'.format(i))

    while len(edges_added) < edges:
        start = 'V{}'.format(randint(0, vertices-1))
        end = 'V{}'.format(randint(0, vertices-1))
        if start != end and end not in graph.vertices[start]:
            graph.add_edge(start, end)
            edges_added.append((start, end))

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    # TODO: limit number of vertices and edges
    # TODO: file name argument
    # TODO: connected components argument
    if len(argv) == 3:
        NUMBER_VERTICES = int(argv[1])
        NUMBER_EDGES = int(argv[2])
        main(NUMBER_VERTICES, NUMBER_EDGES)
    else:
        print('\nError: Graph demo requires two arguments: number of'
              'vertices as an int and the number of edges as an int:\n\n\t'
              'graph_demo.py NUMBER_VERTICES NUMBER_EDGES\n')
