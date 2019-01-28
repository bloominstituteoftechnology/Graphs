"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        #Graph is a set of vertices
        self.vertices = dict() # or {} instead of dict()

    def add_vertex(self, vertex):
        if vertex not in self.vertices.keys():
            self.vertices[vertex] = set()
        return 'vertex already exist...'

    def add_edge(self, start_point, end_point):
        if start_point in self.vertices and end_point in self.vertices:
            #graph is bidirectional.. should add edges back and forth
            self.vertices[start_point].add(end_point)
            self.vertices[end_point].add(start_point) 
        return "vertices not in graph"
    
    
    


