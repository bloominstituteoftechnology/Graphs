"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {

        }
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        
    def add_edge(self, vert_1, vert_2):
        self.vertices[vert_1].add(vert_2)
        self.vertices[vert_2].add(vert_1)
       
        
