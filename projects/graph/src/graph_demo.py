#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from random import sample
from draw import BokehGraph

def main(arg1_vertices=6, arg2_edges=3):
    # pass  # TODO
    """instantiate a graph"""
    my_graph = Graph()
    """add correct number of vertices to graph from input"""
    for num in range(arg1_vertices):
        my_graph.add_vertex(str(num))
    """add edges randomly"""
    for _ in range(arg2_edges):
        random_vertices = sample(my_graph.vertices.keys(), 2)
        my_graph.add_edge(random_vertices[0], random_vertices[1])
    """draw the graph"""
    BokehGraph(my_graph)


if __name__ == '__main__':
    # TODO - parse argv
    if len(argv) == 3:
        ARG1_VERTICES = int(argv[1])
        ARG2_VERTICES = int(argv[2])
        main(ARG1_VERTICES, ARG2_VERTICES)
    else:        
        main()
