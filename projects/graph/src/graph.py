"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, vertex1, vertex2):
        '''
        Add an undirected edge to the graph
        '''
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].edges.add(vertex2)
            self.vertices[vertex2].edges.add(vertex1)
        else:
            raise IndexError("That vertex does not exist.")

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()
    def __repr__(self):
        return f"{self.edges}"

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)