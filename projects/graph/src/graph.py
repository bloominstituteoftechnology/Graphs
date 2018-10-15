"""
Simple graph implementation compatible with BokehGraph class.
"""
from random import random


class Vertex:
    def __init__(self, label, x, y):
        self.label = label
        self.edges = set()
        self.x = x + (random() / 2)
        self.y = y + (random() / 2)

    def __str__(self):
        return f'Vertex {self.label}'


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}
        self.x_mod = 0
        self.y_mod = 0

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex, self.x_mod, self.y_mod)
            self.x_mod += 1
            if self.x_mod == 6:
                self.x_mod = 0
                self.y_mod += 1
        else:
            raise Exception('That vertex already exists')

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception('One or both vertices are not in graph.')
        self.vertices[v1].edges.add(v2)
        self.vertices[v2].edges.add(v1)
