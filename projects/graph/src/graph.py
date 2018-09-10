"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO

class Node:
    def __init__(self):
        self.neighbors = []
    def addNeighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
    def getNeighbors(self):
        return self.neighbors
    def isNeighbor(self, node):
        return node in self.neighbors
