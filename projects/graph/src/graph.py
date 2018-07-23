#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init(self, label):
        self.label = label


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges"""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex.label:
            self.vertices[vertex] = set()
        else:
            raise Exception("This is not a vertex")

    def add_edge(self, start, end, bidirectional = True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)