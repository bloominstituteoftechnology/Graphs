"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex_id):
        self.graph[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].edges.add(v2)
            self.graph[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")

class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    def __str__(self):
        return f"{self.edges}"
   


