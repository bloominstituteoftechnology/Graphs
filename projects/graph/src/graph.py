#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        
    def add_edge(self, start, end, bi = True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertex does not exist')
        self.vetices[start].add(end)
        if bi:
            self.vertices[end].add(start)
        