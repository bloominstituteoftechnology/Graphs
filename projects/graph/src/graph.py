"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """Vertices have a label and a set of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label  # each vertex has a label
        self.edges = set()  # each vertex has a set of multiple edges

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # Start here:
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
    