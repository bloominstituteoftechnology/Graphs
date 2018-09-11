"""
Simple graph implementation compatible with BokehGraph class.
"""
from draw import BokehGraph

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, key, value, bidirectional=True):
        if key not in self.vertices or value not in self.vertices:
            raise Exception(f'No {key} vertex')

        self.vertices[key].add(value)

        if bidirectional:
            self.vertices[value].add(key)



