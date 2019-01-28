"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, new_vertex):
        self.vertices[new_vertex] = set()

    def add_edge(self, vertex_a, vertex_b):
        # add b to a's vertices entry
        self.vertices[vertex_a].add(vertex_b)
        # add a to b's vertices entry
        self.vertices[vertex_b].add(vertex_a)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)