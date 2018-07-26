#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

from draw import BokehGraph

class Graph:
  """Represent a graph as a dictionary of vertices mapping labels to edges."""
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, v):
    if v not in self.vertices:
      self.vertices[v] = set()

  def add_edge(self, start, end):
    if start not in self.vertices or end not in self.vertices:
      raise Exception("Please make sure vertices are in the graph, before creating an edge between them!")
    self.vertices[start].add(end)
    self.vertices[end].add(start)


def test():
  graph = Graph()
  graph.add_vertex('0')
  graph.add_vertex('1')
  graph.add_vertex('2')
  graph.add_vertex('3')
  graph.add_edge('0', '1')
  graph.add_edge('0', '3')
  print(graph.vertices)

  #graph.add_edge('0', '4') # No '4' vertex, should raise an Exception!

  bg = BokehGraph(graph)
  bg.show()

test()