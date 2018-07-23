#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Adjacency list graph."""
    def __init__(self):
        self.vertices = dict()

    def add_edge(self, start, end, bidirectional=True):
        # """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex):
        # if not hasattr(vertex, 'label'):
        #     raise Exception('This is not a vertex!')
        self.vertices[vertex] = set()

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')

graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)