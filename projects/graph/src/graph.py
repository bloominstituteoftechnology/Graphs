#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

g = {
    "0": {"1", "3"},
    "1": {"0"},
    "2": set(),
    "3": {"0"}
}

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = set()

    def add_edge(self, start, end, bidirectional=True):
        pass


    def add_vertex(self, vertex):
        pass
    

