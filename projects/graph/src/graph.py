#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return str(self.label)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self, num_vertices):
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.vertices = [Vertex(str(i)) for i in range(num_vertices)]

    def add_edge(self, x_pos, y_pos, is_bidirectional=True):
        """adds edges to graph"""
        self.matrix[x_pos][y_pos] = 1
        if is_bidirectional:
            self.matrix[y_pos][x_pos] = 1

