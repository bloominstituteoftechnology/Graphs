#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph, Vertex
from random import sample
from draw import BokehGraph

def main(num_vertices=8, num_edges=8):
    graph = Graph()
    for num in range(num_vertices):
        # print(graph.add_vertex(str(num)))
        graph.add_vertex(str(num))
        # print(graph.vertices)
        # for _ in range(num_edges):
            # print(graph.vertices.keys())
    # for num in range(num_vertices):
    #     for _ in range(num_edges):
    #         print(graph.vertices)
            # vertices = sample(graph.vertices.keys(), 2)
            # print(graph.vertices)
            # TODO check if edge already exsists
            # if graph.vertices.values().get_edges() == vertices:
                # graph.add_edge(vertices[0], vertices[1])


# maybe line glyph

    bg = BokehGraph(graph)
        # dir(bg)
        # bg.pos
    bg.show()

if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()
