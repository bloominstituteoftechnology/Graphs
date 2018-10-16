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
    def __init__(self):
        self.vertices = {}
    #ability to add to the dict needed 
    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self.vertices[new_vertex] = set()
        return new_vertex
        
    def add_edge(self, from_vertex, to_vertex):
        new_edge = Edge(to_vertex)
        from_vertex.edges.add(new_edge)#using sets must use add() method
        
        #self.graph_dict[from_vertex] = from_vertex.edges

        
        #add to the edges then we swap the edges that is there
        #out with self.edges though adding might be quicker.
        #not sure copy o(N)  but add is O(1)

        self.vertices[from_vertex].add(new_edge)
        #went with this out of being unsure of line 35
        #I know adding to the set is O(1) for sure though. 
        # A seperate edge case is needed for if to_vertex
        #links from_vertex   this method only handles 
        #one direction 




    
