"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex):
        self.vertices[vertex] = set()

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.vertices:
            if vertex2 in self.vertices:
                self.vertices[vertex1].add(vertex2)

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '2')
graph.add_edge('0', '3')
print(graph.vertices)