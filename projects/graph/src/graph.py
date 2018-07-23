#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
  def __init__(self, label):
    self.label = label
    self.edges = Object()

  def __repr__(self):
    return str(self.label)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
      self.vertices= set()

    def add_edge(self, start, end, bidirectional= true):
      if start not in self.vertices or end not in self.vertices:
        raise Exception ('Error vertices not in graph')
      start.edges.add(end)
      if bidirectional:
        end.ed

