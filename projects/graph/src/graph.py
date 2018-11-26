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

    # add a bidirectional edge 
    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].add(to_vertex)
            self.vertices[to_vertex].add(from_vertex)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)