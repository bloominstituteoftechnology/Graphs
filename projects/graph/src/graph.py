#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vert(self, vertex, edges=()):
        if not set(edges).issubset(self.vertices):
            raise Exception("can't have edge to non-existant vertex")
        self.vertices[vertex] = set(edges)
    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('u stoopid?')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)
