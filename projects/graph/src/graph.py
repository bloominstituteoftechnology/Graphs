"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices.update({value: set()})

    def add_edge(self, vertex1, vertex2):
        if self.vertices.get(vertex1) != None and self.vertices.get(vertex2) != None:
            self.vertices.get(vertex1).add(vertex2)
            self.vertices.get(vertex2).add(vertex1)
        else:
            raise Exception('Nonexistent vertex.')
