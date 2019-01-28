"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, value):
        self.vertices[value] = set()
