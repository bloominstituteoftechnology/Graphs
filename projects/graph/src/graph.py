"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertexList = {}

    def vertices(self):
        return self.vertexList

    def add_vertex(self, vertex):
        self.vertexList[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertexList:
            self.vertexList[vertex1].add(vertex2)
        else:
            self.vertexList[vertex1] = [vertex2]