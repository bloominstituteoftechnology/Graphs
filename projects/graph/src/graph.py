"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = {}
    def add_vertex(self, vert_id):
        self.vertices[vert_id] = Vertex(vert_id)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("One or both of these vertices does not exist!")
class Vertex:
    def __init__(self, vert_id, x=None, y=None):
        self.id = vert_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    def __repr__(self):
        return "{}".format(self.edges)