"""
Simple graph implementation
"""
test_graph =  { 
    "A": {"B"},
    "B": {"C", "D"},
    "C": {"E"},
    "D": {"F", "G"},
    "E": {"C"},
    "F": {"C"},
    "G": {"A", "F"}
                }
        

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        print(self.vertices)
        
    
    def add_edge(self, from_vertex, to_vertex):
        self.vertices[from_vertex].add(to_vertex)
    
    def add_vertex(self, value):
        self.vertices[value] = set()

