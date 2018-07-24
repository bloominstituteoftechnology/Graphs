#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """
    Represent a single vertex that is aware of all existing verrtices
    """
    all_vertices = set()

    def __init__(self, label, edges=()):
        if label in Vertex.all_vertices:
            raise Exception('Error: vertex {} already exists'.format(label))
        if not set(edges).issubset(Vertex.all_vertices):
            raise Exception('Error: cannot create edge to nonexistent vertex')
        self.label = label
        self.edges = set(edges)
        Vertex.all_vertices.add(self.label)

    def __repr__(self):
        return str(self.label)

    def add_edge(self, end):
        """
        Add edge to vertex if vertex exists and edge does not already exist
        """
        if end.label not in Vertex.all_vertices:
            raise Exception('Error: cannot create edge to nonexistent vertex')
        if end in self.edges:
            raise Exception('Error: Edge already exists')
        self.edges.add(end)


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=True):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)
        else:
            raise Exception('Vertex does not exist')
