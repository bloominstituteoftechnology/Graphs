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
        self.vertices = set()
    
    def add_vertex(self, item):
        self.vertices.add(item)
    
    def add_edge(self, start, end, is_directed = False):
        start.edges.add(end)
        if not is_directed:
            end.edges.add(start)

my_gr = Graph()
v1 = Vertex('A')
v2 = Vertex('B')

my_gr.add_vertex(v1)
my_gr.add_vertex(v2)