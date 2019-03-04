"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        pass  # TODO

    def add_vertex(self, vert):
        if self.vertices.vert:
            return False
        else:
            return self.vertices.append(vert)

    def add_edge(self, vert, edge):
        if self.vertices.vert:
            return self.vertices.vert.append(edge)
        else:
            return False
