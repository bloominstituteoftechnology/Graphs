"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = { }

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex_a, vertex_b):
        if vertex_a in self.vertices.keys() and vertex_b in self.vertices.keys():
            self.vertices[vertex_a].add(vertex_b)
            self.vertices[vertex_b].add(vertex_a)
        else:
            print("Cannot find all vertices")



graph = Graph() #my graph instance
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('4', '3')

print(graph.vertices)
