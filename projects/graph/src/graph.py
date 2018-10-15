"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed
    #ability to add to the dict needed 
    def add_vertex(self, vertex):
        self.graph_dict[vertex] = set()
        
    def add_edge(self, from_vertex, to_vertex):
        self.graph_dict[from_vertex] = to_vertex
        self.graph_dict[to_vertex] = from_vertex

    
