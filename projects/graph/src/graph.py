"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
  

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def add_vertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    