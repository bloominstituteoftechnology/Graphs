"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}
    def add_vertex(self,vertex_id):
        self.vertices[vertex_id]=Vertex(vertex_id)
    def add_edge(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError('Unable to locate vertex')
        

class Vertex:
    def __init__(self,vertex_id):
        self.id=vertex_id
        self.edges=set()
    def __repr__(self):
        return f'{self.edges}'