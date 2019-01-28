"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vertex1, vertex2):
        if self.vertices[vertex1] and self.vertices[vertex2]:
            self.vertices[vertex1].add(vertex2)
