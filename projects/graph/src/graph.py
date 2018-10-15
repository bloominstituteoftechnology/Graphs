"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph: 
            self.graph[vertex] = []
    
    def add_edge(self, vertex, edge):
        if 


graph = Graph()
graph.add_vertex('0')