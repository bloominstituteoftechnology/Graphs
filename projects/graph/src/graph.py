#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[str(vertex)] = set()
    
    def add_edge(self, start, end):
        start = str(start)
        end = str(end)
        if not start in self.vertices or not end in self.vertices:
            raise Exception('Vertex does not exist!')
        else:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
    
    def __repr__(self):
        for vertex in self.vertices:
            print({f'Vertex {vertex} is connected to {self.vertices[vertex]}'})