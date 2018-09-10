"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            print("That vertex already exists")
            return False
        else:
            self.vertices[vertex] = set()        

    def add_edge(self, startpoint, endpoint):
        if startpoint not in self.vertices or endpoint not in self.vertices:
            print("Invalid start or endpoint")
            return False
        else:
            self.vertices[startpoint].add(endpoint)
            self.vertices[endpoint].add(startpoint)

