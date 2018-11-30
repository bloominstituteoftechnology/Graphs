"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = Vertex(vertex)

    def add_edge(self, vertex_one, vertex_two):
        # first_index = vertices.index(vertex_one)
        self.vertices[vertex_one].edge.add(vertex_two)
        # second_index = vertices.index(vertex_two)
        self.vertices[vertex_two].edge.add(vertex_one)

class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.edge = set()

    def __repr__(self):
        return f"{self.vertex} : {self.edge} \n"

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
