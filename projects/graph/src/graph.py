"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, a):
        self.vertices[a] = set()
        pass

    def add_edge(self, a, b):
        if(a not in self.vertices):
            self.add_vertex((a))
            self.vertices[a] = set(b)
        elif(a in self.vertices):
            self.vertices[a]
        pass

    def get_vertices(self):
        print(self.vertices)
        return self.vertices



g = Graph()
g.add_vertex("0")
g.add_vertex("1")
g.add_edge()
g.get_vertices()