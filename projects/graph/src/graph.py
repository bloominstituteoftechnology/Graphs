#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, item):
        self.vertices.update({item.label: item.edges})

    def add_edge(self, start, end, is_directed=False):
        start.edges.add(end.label)
        if not is_directed:
            end.edges.add({start.label})
