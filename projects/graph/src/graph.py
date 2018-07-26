"""
Simple graph implementation compatible with BokehGraph class.
"""

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