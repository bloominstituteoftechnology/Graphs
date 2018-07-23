#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = set()

    def add_vertex(self, vertex):
        # if not hasattr(vertex, 'label'):
        #     raise Exception('This is not a vertex!')
        self.vertices.add(vertex)

    def add_edge(self, start, end, bidirectional=True):
        # if start not in self.vertices or end not in self.vertices:
        #     raise Exception('Error - vertices not in graph!')
        start.vertices.add(end)
        if bidirectional:
            end.vertices.add(start)

# test
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)