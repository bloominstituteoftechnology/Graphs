"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, str_id):
        name = str(str_id)
        self.vertices[name] = Vertex(name)
    
    def add_edge(self, vertex, dest):
        self.vertices[vertex].edges.add(dest)
        self.vertices[dest].edges.add(vertex)
"""
new_vertex = Vertex('1')
"""
class Vertex:
    def __init__(self, id, X=None, Y=None):
        self.id = id
        self.edges = set()
        if X == None:
            self.x = random.random() * 10 - 5
        else:
            self.x = X
        if Y == None:
            self.y = random.random() * 10 - 5
        else:
            self.y = Y
    
    def __repr__(self):
        return f"Vertex {self.id}"

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
    
    






