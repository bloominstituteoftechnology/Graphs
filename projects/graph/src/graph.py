"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # store vertices in dictionary
        self.vertices = {}

    # add a vertex which is an empty set
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
print(graph.vertices)