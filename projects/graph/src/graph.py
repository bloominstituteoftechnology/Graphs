"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # self.vertices = vertices
        self.vertices = {}
    def add_vertex(self,vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    # def add_vertex(self,vertex):
    #     self.vertices.update({str(vertex): set()})
    #     print(f"Second line -> {self.vertices}")
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2].edges.add(v2)
            self.vertices[v1].edges.add(v1)
        else:
            raise (IndexError("That vertex doesn't exist"))
    # def add_edge(self, vertex, edge):
    #     self.vertices.update({str(vertex): {str(node) for node in edge} })
    #     print(f"Third line -> {self.vertices}")

class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x == None:
            self.x = random.random() * 10-5
        else:
            self.x = x
        if y == None:
            self.y= random.random() * 10-5
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

# graph = Graph({'0': {'1', '3'},'1': {'0'},'2': set(),'3': {'0'}})

# print(f"First line -> {graph.vertices}") First line
# graph.add_vertex(8) Second Line
# graph.add_edge(2, [1,2,3]) #hird line

