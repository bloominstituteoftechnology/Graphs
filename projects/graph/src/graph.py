"""
Simple graph implementation compatible with BokehGraph class.
"""
from random import random


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()
        self.x = random() * 5
        self.y = random() * 5

    def __str__(self):
        return f'Vertex {self.label}'


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)
        else:
            raise Exception('That vertex already exists')

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception('One or both vertices are not in graph.')
        self.vertices[v1].edges.add(v2)
        self.vertices[v2].edges.add(v1)

    def get_nodes(self):
        x = []
        y = []
        for vertex in self.vertices:
            x.append(self.vertices[vertex].x)
            y.append(self.vertices[vertex].y)
        return zip(x, y)

    def get_edges(self):
        s = []
        e = []
        checked = set()
        for vertex, edges in self.vertices.items():
            if vertex not in checked:
                for connection in edges.edges:
                    s.append(vertex)
                    e.append(connection)
                checked.add(vertex)
        return dict(start=s, end=e)
