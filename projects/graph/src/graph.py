#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO

    def add_vortex(self, v):
        if v not in self.vertices:
            self.vertices[v] = set()
        else:
            raise ValueError("")

    def add_edge(self, start, end, biderectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("")
        else:
            self.vertices[start].add(end)
            if biderectional = True:
                self.vertices[end].add(start)