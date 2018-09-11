"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.colors = {}
        self.x_positions = {}
        self.y_positions = {}

    def add_vertex(self, vertex, x = 0, y = 0, color = "#999"):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
            self.colors[vertex] = color
            self.x_positions[vertex] = x
            self.y_positions[vertex] = y
        else:
            raise Exception("This vertex has already been added")

    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
        else:
            raise Exception("One of your vertices doesn't exist")