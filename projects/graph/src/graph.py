"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        #check if an object with label already exists
        if label in self.vertices:
            raise ValueError(f"Duplicate vertex '{label}' found")
        #create new vertex object with the label passed to function
        self.vertices[label] = set()