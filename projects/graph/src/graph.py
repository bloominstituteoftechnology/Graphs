"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self,label):
        self.vertices = {}
        self.label = label
        self.edges = ()

    def add_vertex(self,key):
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self,key):
        return self.vertices[key]

    def add_edge(self, srcKey, destKey, weight):
        self.vertices[srcKey].addNextEdge(self.vertices[destKey],weight)

    def Edge_doesNot_exist(self, srcKey, destKey, weight):
        return self.vertices[srcKey].whoDoes_itPointTo(self.vertices[destKey], weight)

    def __iter__(self):
        return iter(self.vertices.values())

class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def addNextedge(self, dest, weight):
        self.points_to[dest] = weight

    def getNextEdge(self):
        return self.points_to.keys

    def whoDoes_itPointTo(self,dest):
        return dest in self.points_to
