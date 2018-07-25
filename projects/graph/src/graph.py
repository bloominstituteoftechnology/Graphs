"""
Simple graph implementation compatible with BokehGraph class.
"""

"""
initial
"""

class Vertex: 
    def __init__ (self, label):
        """ using init to initialize self.label and edge"""
        self.label = label
        self.edge = set()
    def __repr__ (self): 
        """ using repr method to change label"""
        return str(self.label)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end, bidirectional= True):
        """adding edge from start to end""" 
        if start not in self.vertices or end not in self.vertices:
            raise Exception('raiseError vertices not found in graph')
        else:
            self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
