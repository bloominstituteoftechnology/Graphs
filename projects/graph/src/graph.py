#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

 class Vertex:
    def __init__(self, label):
      self.label = label
      self.edges = set()

    def __repr__(self):
      return str(self.label)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
   def __init__(self):
      self.vertices = set() 

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
          raise Exception('Error - vertices not in graph!')
        start.edges.add(end)
        self.vertices[start] = 1
        if bidirectional: 
          end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices.add(vertex)