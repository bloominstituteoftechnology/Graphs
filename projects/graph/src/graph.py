"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self, size):
        self.size = size
        self.vertices = [[] for i in range(size)]

    def add_edge(self, i, j):
        if not (i in self.vertices[j]):
            self.vertices[j].append(i)
            self.vertices[i].append(j)
