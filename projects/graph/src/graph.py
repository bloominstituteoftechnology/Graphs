#!/usr/bin/python
"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def create_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = set()
        else:
            raise ValueError('This vertex has already been created')

    def create_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('%s or %s has not been created' % (start, end))
        else:
            self.vertices[start].add(end)

graph = Graph()
graph.create_vertex('0')
graph.create_vertex('1')
graph.create_vertex('2')
graph.create_vertex('3')
graph.create_edge('0', '1')
graph.create_edge('2', '3')
print(graph.vertices)