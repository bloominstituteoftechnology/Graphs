#!/usr/bin/python
#Start Here

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()
    
    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('Error -- This is not a vertex!')
            self.vertices[vertex] = set()

class Vertex:
    def __init__(self, label, bidirectional=True):
        self.label = label
        self.edge = set()

class Edge:
    def __init__(self, destination, bidirectional=True):
        self.destination = destination
