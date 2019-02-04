"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {

        }
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        pass
    def add_edge(self):
        pass
        
