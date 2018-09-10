"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex, edges=None):
        self.vertices[vertex] = set(edges)
    def add_edge(self, head, tail):
        self.vertices[head].add(tail)
        self.vertices[tail].add(head)