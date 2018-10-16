"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3)
        if self.y is None:
            self.y = 2 * (self.id // 3) + self.id / 10 * (self.id % 3)
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            colorString = "#"
            for i in range(0, 3):
                colorString += hexValues[random.randint(0,len(hexValues) - 1)]
            self.color = colorString
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return f"{self.vertices}"

    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            raise Exception('Error: That vertex already exists')
        else:
            self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, start, end):
        if start not in self.vertices:
            raise Exception('Error: Start vertex not found')
        if end not in self.vertices:
            raise Exception('Error: End vertex not found')
        else:
            self.vertices[start].edges.add(end)
            self.vertices[end].edges.add(start)

    def add_directed_edge(self, start, end):
        if start not in self.vertices:
            raise Exception('Error: Start vertex not found')
        if end not in self.vertices:
            raise Exception('Error: End vertex not found')
        else:
            self.vertices[start].edges.add(end)
