"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices/nodes mapping labels to edges."""
    def __init__(self, num_vertices):
        self.matrix = {}

    def connect_vertex(self, row, col):


