#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, label):
        self.vertices.update(label=set())
    def add_edge(self, from_vertex, to_vertex):
        self.vertices[from_vertex].add(to_vertex)


