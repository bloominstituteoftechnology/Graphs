"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        """
        Create the empty graph
        """
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph
        """
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else: 
            raise IndexError("That vertex does not exist")

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()
    def __repr__(self):
        return (f'{self.edges}')

graph = Graph()  
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '4') # Should throw error
print(graph.vertices)