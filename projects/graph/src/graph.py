#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertice):
        self.graph[ vertice ] = set()

    def add_edge(graph):
        edges = []
        

graph = Graph()

graph.add_vertex('1')
graph.add_vertex('2')
print(graph.graph)