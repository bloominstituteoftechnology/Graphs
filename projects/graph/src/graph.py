"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, v):
        self.vertices[v] = set()
    def add_edge(self, v, e):
        self.vertices[v].add(e)
        self.vertices[e].add(v)


