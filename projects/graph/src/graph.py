"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise Exception('Error: That vertex already exists')
        else:
            self.vertices[vertex] = set()
    def add_edge(self, start, end):
        if start not in self.vertices:
            raise Exception('Error: Start vertex not found')
        if end not in self.vertices:
            raise Exception('Error: End vertex not found')
        else:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
