"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} #nodes
        # self.edges = edges
        # self.weight = weight

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)




