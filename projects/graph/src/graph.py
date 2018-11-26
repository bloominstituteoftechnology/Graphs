"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, n):
        self.name = n
        self.children = list()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
