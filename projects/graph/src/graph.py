"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []


class Node:
    def __init__(self):
        self.neighbors = []
    # O(1)

    def addNeighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
    # O(1)

    def getNeighbors(self):
        return self.neighbors
    # O(n)

    def isNeighbor(self, node):
        return node in self.neighbors
