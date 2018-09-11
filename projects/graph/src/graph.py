"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def addVertex(self, vertexID):
        self.vertices[vertexID] = set()
    
    def addEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")


class Node:
    def __init__(self):
        self.neighbors = []

    def addNeighbor(self, newNode):
        self.neighbors.append(newNode)

    def getNeighbors(self):
        return self.neighbors

    def isNeighbor(self, node):
        return node in self.neighbors

    