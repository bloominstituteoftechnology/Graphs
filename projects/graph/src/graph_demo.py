#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from random import sample
from sys import argv
from graph import Vertex, Graph
from draw import BokehGraph

def main(num_vertices, num_edges, draw_components=True):
    graph = Graph()
    for num in range(num_vertices):
        graph.add_vertex(num)

    for _ in range(num_edges):
        vertex1 = sample(graph.vertices.keys(), 1)[0]
        vertex2 = sample(graph.vertices.keys(), 1)[0]
        graph.add_edge(vertex1, vertex2)

    bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    bokeh_graph.draw()

if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
    else:
        print('Expected arguments: num_verts num_edges draw_components ')
        print('Both numbers should be integers, draw_components should be 0/1')