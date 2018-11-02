"""
Simple graph implementation compatible with BokehGraph class.
"""

from enum import Enum

class Vertex:
  def __init__(self, label, component=-1):
    self.label = label
    self.component = component

  def __str__(self):
    return str(self.label)

  def __repr__(self):
    return str(self.label)

class SearchMethod(Enum):
  BFS = 0
  DFS = 1

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

  def search(self, root, method=SearchMethod.BFS, component=-1):
    collection = [root]
    marked = set([root])
    index = 0 if method == SearchMethod.BFS else -1

    while len(collection) > 0:
      v = collection.pop(index)
      v.component = component
      for each in self.vertices[v]:
        if each not in marked:
          collection.append(each)
          marked.add(each)

    return marked

  def connected_components(self):
    connected = []
    visited = set()
    for v in self.vertices:
      if v not in visited:
        component = self.search(v, component=len(connected))
        connected.append(component)
        visited.update(component)

    return len(connected)