"""
Simple graph implementation compatible with BokehGraph class.
"""

import random
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def addVertex(self, vertexID):
        self.vertices[vertexID] = set()
    
    def addEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            # if v1 not in v2 and v2 not in v1:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
            # v1.addNeighbor(v2)
            # v2.addNeighbor(v1)
            
        else:
            raise IndexError("That vertex does not exist")

    def getRandomOtherVertex(self, v1):
        v2 = v1
        key = None
        while v2 is v1:
            keys = list(self.vertices)
            randKey = keys[random.randint(0, len(keys)-1)]
            
            v2 = self.vertices[randKey]
            key = randKey
        return randKey



class Node:
    def __init__(self):
        self.neighbors = []

    def addNeighbor(self, newNode):
        self.neighbors.append(newNode)

    def getNeighbors(self):
        return self.neighbors

    def isNeighbor(self, node):
        return node in self.neighbors

    