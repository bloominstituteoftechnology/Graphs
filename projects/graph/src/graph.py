#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


"""Graph representation using adjacency list."""

class Edge:
    """Edges in the adjacency list are just a destination."""
    # Using simple classes for illustrative purposes
    # pylint: disable=too-few-public-methods
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    """Vertices have a label and a set of edges."""
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)


class Graph:
    """Adjacency list graph."""
    def __init__(self):
        self.Vertex = {}

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.Vertex or end not in self.Vertex:
            raise Exception('Error - vertices not in graph!')
        self.Vertex[start].edges.add(end)
        print(start)
        print(self.Vertex[start].edges)
        if bidirectional:
            self.Vertex[end].edges.add(start)

    def add_vertex(self, vertex):
        self.Vertex[vertex] = Vertex(vertex)



graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.Vertex)