"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # store vertices in dictionary
        self.vertices = {}

    # add a vertex
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    # add a bidirectional edge 
    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].edges.add(to_vertex)
            self.vertices[to_vertex].edges.add(from_vertex)

    # add a unidirectional edge 
    def add_directed_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].edges.add(to_vertex)

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
