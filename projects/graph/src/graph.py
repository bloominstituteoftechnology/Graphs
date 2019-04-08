"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices={}):
        self.vertices = vertices

    def add_vertex(self, verNum):
        self.vertices[verNum] = set()

    def add_directed_edge(self, verNum, edgeNum):
        if verNum not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (verNum))
        elif edgeNum not in self.vertices: # Stretch, O(1)
            raise ValueError("No %s vertex" % (edgeNum))
        self.vertices[verNum].add(edgeNum)

