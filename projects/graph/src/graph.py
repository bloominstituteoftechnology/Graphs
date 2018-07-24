#!/usr/bin/python
"""Graph representation using adjacency list."""
class Vertex:
    """Vertices have a label and a set of edges."""
    def __init__(self, label):
        self.label = label
        self.edges = {}

    def __repr__(self):
        return str(self.label)

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:    
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise Exception("Error: vertex already exists!")
        self.vertices[vertex] = set()
    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("supplied vertex not in graph!!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

graph = Graph()
v1 = Vertex('A')
v2 = Vertex('B')
v3 = Vertex('C')

graph.add_vertex(v1)
graph.add_vertex(v2)
graph.add_vertex(v3)

graph.add_edge(v1,v2,bidirectional=True)
graph.add_edge(v1, v3, bidirectional=True)

print(graph.vertices)
