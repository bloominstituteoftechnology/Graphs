#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        self.vertices[label] = set()

    def add_edge(self, start, end, bidirectional=True):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
        else:
            raise ValueError("Please provide start and end vertices that exist.")
        if bidirectional:
            self.vertices[end].add(start)
