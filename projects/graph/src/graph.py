"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, value):
        self.node = value
        self.edges = set() 

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verticies = {}
    def add_vertex(self, vertex_id):
        self.verticies[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)
            self.verticies[v2].add(v1)
        else:
            raise IndexError("No vertex!")


