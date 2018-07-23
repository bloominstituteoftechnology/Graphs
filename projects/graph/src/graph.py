#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,vertex):
        self.vertices[vertex] = set()

    def add_edge(self, start_index, end_index, bidirectional=True) :
        self.vertices[start_index].add(end_index)
        if bidirectional:
            self.vertices[end_index].add(start_index)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
