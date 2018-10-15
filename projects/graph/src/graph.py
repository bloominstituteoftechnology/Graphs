"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self,value):
        self.value = value 
        self.edges = set()

    def add_edge(self, vertex):
        self.edges.add(vertex)
    
    def get_edges(self):
        return self.edges.keys()
    
class Edge:
    def __init__(self, destination, weight = 0):
        self.destination = destination
        self.weight = weight 

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed
    #ability to add to the dict needed 
    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self.graph_dict[new_vertex] = set()
        
    def add_edge(self, from_vertex, to_vertex):
        self.graph_dict[from_vertex].add(to_vertex)
        self.graph_dict[to_vertex].add(from_vertex)
        #not sure on this at the moment seems like 
        # the same thing twice though the instructions say 
        # to build a dictionary best practice is to have Edge
        # and Vertex classes 
        from_vertex.add_edge(to_vertex)
        to_vertex.add_edge(from_vertex)



    
