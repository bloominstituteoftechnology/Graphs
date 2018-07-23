#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        def __init__(self):
        self.graph = {}

    def add_vertex(self, vertice):
        self.graph[ vertice ] = set()

    def add_edge(self, node, connect_node):
        self.graph[ node ].add(connect_node)

graph = Graph()

graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')

graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
graph.add_edge('2', '3')
graph.add_edge('3', '1')

print(graph.graph)
