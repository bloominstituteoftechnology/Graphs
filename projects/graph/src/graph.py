"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        if not label in self.vertices:
            self.vertices[label] = set()

    def add_edge(self, vertex, destination):
        if vertex in self.vertices and destination in self.vertices:
            self.vertices[vertex].add(destination)
            self.vertices[destination].add(vertex)


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '4')
print(graph.vertices)