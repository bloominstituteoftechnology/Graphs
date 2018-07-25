#!/usr/bin/python
"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, edges=()):
        # Add a new vertex, optionally with edges to other vertices. 
        if vertex in self.vertices: 
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices): 
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        # Add a edge (default bidirectional) between two vertices. 
        if start not in self.vertices:
            raise Exception('Error: The start vertice is not in the graph.')
        elif end not in self.vertices:
            raise Exception('Error: The end vertice is not in the graph.')

        self.vertices[start].add(end)

        if bidirectional:
            self.vertices[end].add(start)