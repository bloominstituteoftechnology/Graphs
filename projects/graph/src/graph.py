"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    # def add_vertex(self, v):
    #     self.vertices[v] = set()
    def add_vertex(self, v):
        self.vertices[v] = Vertex(v)
    def add_edge(self, v1, v2):
        self.vertices[v1].edges.add(v2)
        self.vertices[v2].edges.add(v1)

class Vertex: 
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x is None: 
            self.x = random.random() * 10 
        else: 
            self.x = x
        if y is None: 
            self.y = random.random() * 10 
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

