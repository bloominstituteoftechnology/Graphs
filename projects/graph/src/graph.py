"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vertex, value):
        # Add edge as a value to the vertex
        self.vertices[vertex].add(value)
        # Add vertex as a value to the edge
        self.vertices[value].add(vertex)
