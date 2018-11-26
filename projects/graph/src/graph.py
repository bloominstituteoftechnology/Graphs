"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        vertices = []

    def add_vertex(self, vertex):
        self.vertices.append(Vertex(vertex))

    def add_edge(self, vertex_one, vertex_two):
        first_index = vertices.index(vertex_one)
        vertices[first_index] = {vertex_one, vertex_two}
        second_index = vertices.index(vertex_two)
        vertices[second_index] = {vertex_two, vertex_one}

class Vertex:
    def __init__(self, vertex, edge=set()):
        self.vertex = vertex
        self.edge = edge
