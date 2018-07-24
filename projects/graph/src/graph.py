#!/usr/bin/python

from collections import defaultdict

"""
Simple graph implementation compatible with BokehGraph class.
"""


# class Vertex:
#     """Vertices have a label and a set of edges."""

#     def __init__(self, label):
#         self.label = label
#         self.edges = set()

#     def __repr__(self):
#         return str(self.label)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = defaultdict(set)

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error - vertices not in graph!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()


graph = Graph()
graph.add_vertex("0")
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_edge("0", "1")
graph.add_edge("0", "3")
print(graph.vertices)