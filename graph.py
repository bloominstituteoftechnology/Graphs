#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

from sys import argv
from draw import BokehGraph


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices."""
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, vertex_a, vertex_b, bidirectional=True):
        """Add a edge (default bidirectional) between two vertices."""
        if vertex_a not in self.vertices or vertex_b not in self.vertices:
            raise Exception('Vertices to connect not in graph!')
        self.vertices[vertex_a].add(vertex_b)
        if bidirectional:
            self.vertices[vertex_b].add(vertex_a)


def main(num_vertices=8, num_edges=8):
    """Build demo graph and draw."""
    graph = Graph()
    for num in range(num_vertices):
        graph.add_vertex(str(num))

    # Add some random edges
    from random import sample
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        graph.add_edge(vertices[0], vertices[1])

    bokeh = BokehGraph(graph)
    bokeh.show()


if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = argv[1]
        NUM_EDGES = argv[2]
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()  # accept defaults
