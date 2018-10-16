#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random
from sys import argv
from graph import Graph
from draw import BokehGraph

def main(num_vertices=None, num_edges=None):
    if num_vertices is None:
        num_vertices = random.randint(1, 20)
    else:
        num_vertices = int(num_vertices)
    if num_edges is None:
        num_edges = num_vertices
    elif int(num_edges) > num_vertices*(num_vertices-1)/2:
        num_edges = num_vertices
    else:
        num_edges = int(num_edges)
    
    # build graph
    graph = Graph()
    for num in range(num_vertices):
        graph.add_vertex(str(num))

    # Add some random edges
    from random import sample
    for _ in range(num_edges):
        vertices = sample(list(graph.vertices), 2)
        graph.add_edge(vertices[0], vertices[1])

    print(graph.vertices)
    bg = BokehGraph(graph)
    bg.draw()


if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = argv[1]
        NUM_EDGES = argv[2]
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()
