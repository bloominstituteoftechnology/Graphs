"""
Simple graph implementation
"""
#initial commit

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # add a dictionary of vertices
        self.vertices = {}
    # placeholders for add_vertex and add_edge methods
    # add_vertex needs only a vertex, while add_edge needs both a vertex and edge
    def add_vertex(self, vertex):
        self.vertices[vertex] = {}
        
    def add_edge(self, vertex, edge):
        pass #TODO