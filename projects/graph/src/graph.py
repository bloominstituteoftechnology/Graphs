"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
     #   self.id
        self.vertices = {}
        vertices = self.vertices
        # self.label = label
        self.edges = ()
    # self.vertices[key] = Vertex[key]
    #  key is vertex_id

    def add_vertex(self,key):
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self,key):
        return self.vertices[key]

    def add_edge(self, srcKey, destKey):
        if srcKey in self.vertices and destKey in self.vertices:
            self.vertices[srcKey].edges.add(destKey)
            self.vertices[destKey].edges.add(srcKey)
        else:
            raise IndexError("That vertex does not exist!")
    # def add_edge(self, srcKey, destKey):
    #     self.vertices[srcKey].addNextEdge(self.vertices[destKey])
    #
    # def Edge_doesNot_exist(self, srcKey, destKey):
    #     return self.vertices[srcKey].whoDoes_itPointTo(self.vertices[destKey])
    #
    # def __iter__(self):
    #     return iter(self.vertices.values())

class Vertex:
    def __init__(self, key, x=None, y=None):
        self.key = key
        self.edges = set()
        self.points_to = {}
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    # def addNextedge(self, dest):
    #     self.points_to = dest
    #
    # def getNextEdge(self):
    #     return self.points_to.keys
    #
    # def whoDoes_itPointTo(self,dest):
    #     return dest in self.points_to

    def __repr__(self):
        return f"{self.edges}"

graph = Graph() # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
print(graph.vertices)
