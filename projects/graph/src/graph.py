"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {
            0: {1, 2},
            1: {1},
            2: {0}
        }
    def add_vertex(self, name):
        self.vertices[name] = set()

    def add_edge(self, vertex1, vertex2):
        self.vertices[vertex1].add(vertex2)

