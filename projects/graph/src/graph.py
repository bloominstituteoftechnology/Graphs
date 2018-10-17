"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, label):
        self.vertices[label] = (Vertex(label))

    def show_graph(self):
        return self.vertices

    def add_edge(self, vertex, destination):
        vert = self.vertices[vertex]
        vert.edges.add(Edge(destination))

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

class Edge:
    def __init__(self, destination):
        self.destination = destination
