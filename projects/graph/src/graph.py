#!/usr/bin/python
"""Graph representation using adjacency list."""
class Vertex:
    """Vertices have a label and a set of edges."""
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:    
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = set()

    def add_vertex(self, vertex):
        vertex = Vertex()
        # if not hasattr(vertex, 'label'):
        #     raise Exception('This is not a vertex!')
        self.vertices.add(vertex)
    def add_edge(self, start, end, bidirectional=True):
        # if start not in self.vertices or end not in self.vertices:
        #     raise Exception("supplied vertex not in graph!!")
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

