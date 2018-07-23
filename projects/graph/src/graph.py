#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = set()
        else:
            raise ValueError("that vertex already exists in the graph")

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("%s or %s does not exist" %(start, end))
        else:
            self.vertices[start].add(end)
            if bidirectional == True:
                self.vertices[end].add(start)