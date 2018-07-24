#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vortex(self, vertex, edges=set()):
        if vertex not in self.vertices:
            self.vertices[vertex] = set(edges)
        else:
            raise ValueError("Vertice not found")

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Verices not connecting in graph")
        else:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)

graph = Graph()

