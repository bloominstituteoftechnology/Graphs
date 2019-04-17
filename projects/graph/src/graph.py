"""
Simple graph implementation
"""
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
       self.vertices = {}
       
    def add_vertex(self, key):
        self.vertices[key] = []
        return self.vertices[key]

    def add_edge(self, key, t):
        if key not in self.vertices or t not in self.vertices:
            print('Vertex could not be faund!')
        else:   
            self.vertices[key].append(t)
            return self.vertices[key]
