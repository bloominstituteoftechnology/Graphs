"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, a):
        if (a not in self.vertices):
            self.vertices[a] = set()
        else:
            return print("Already a vertex")


    def add_edge(self, a, b):
        print(a)
        if(b not in self.vertices):
            print(f"Node {b} is not in vertex")
        else:
            self.vertices[a].add(b)
            print(self.vertices)

    def get_vertices(self):
        print(self.vertices)
        return self.vertices

