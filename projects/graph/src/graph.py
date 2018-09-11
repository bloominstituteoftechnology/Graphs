"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise Exception(f'vertex {vertex} already exists')
        
        self.vertices[vertex] = set()
    
    def add_edge(self, vertex1, vertex2):
        if not vertex1 in self.vertices:
            raise Exception(f'vertex1: {vertex1} does not exist')
        
        if not vertex2 in self.vertices:
            raise Exception(f'vertex2: {vertex2} does not exist')

        self.vertices[vertex1].add(vertex2)
        self.vertices[vertex2].add(vertex1)
    
    def add_directional_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices[vertex2]:
            raise Exception(f'Use the add_edge method instead')
        self.vertices[vertex1].add(vertex2)