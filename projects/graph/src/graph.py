"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, parent, child):
        if parent in self.vertices and child in self.vertices:
            self.vertices[parent].add(child)
        else:
            print("One or more vertices, not in graph")
