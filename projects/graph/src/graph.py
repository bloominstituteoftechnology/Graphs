#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """Object representation of Vertex"""
    def __init__(self, label):
        self.label = label
        self.edges = set()

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        """Add anew vertex, optionally with edges to other vehicles."""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional = True):
        """Add a edge (default bidrectional) between two vertices."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph!')    
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

def main(): #instantiate your graph
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

    if __name__ == '_main_':
        main()

