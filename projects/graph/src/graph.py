#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
graph1 = {
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
    # TODO
        self.vertices = {}

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Start and or end doesn't exist here")
        else:
            self.vertices[start].add(end)
            if bidirectional == True:
                self.vertices[end].add(start)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError("that vertex already exists")


