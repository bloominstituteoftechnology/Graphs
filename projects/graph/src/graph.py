#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """ Vertices always have a label and a set of edges. """
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)

class Graph:    
    """ Represent a graph as a dictionary of vertices mapping labels to edges. """
    """ Type of graph: adjacency list """
    def __init__(self):
        self.vertices = set()

    def add_edge(self, start, end, bidirectional=True):
        """ Adding an edge from start to end. """
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error: vertices not in graph!")
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices.add(vertex)

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)