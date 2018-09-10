"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def add_neighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def add_vertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def add_edge(self, f, t, cost = 0):
        if f not in self.vertices:
            nv = self.add_vertex(f)
        if t not in self.vertices:
            nv = self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], cost)  


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)