"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}
    def add_vertex(self,vertex):
        self.vertices[vertex]=set()
    def add_edge(self,vertex,edge):
        try:
            if self.vertices[edge] is not None:
                self.vertices[vertex].add(edge)
                self.vertices[edge].add(vertex)
        except:
            print('No such vertex exists.')
        

