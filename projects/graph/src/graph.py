"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        if v1 and v2 in self.vertices:
            self.vertices[v1].update(v2)
            self.vertices[v2].update(v1)
        if v1 not in self.vertices:
            raise Exception("v1 is not in self.vertices")
        if v2 not in self.vertices:
            raise Exception("v2 is not in self.vertices")