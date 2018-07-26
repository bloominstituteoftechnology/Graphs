"""
Simple graph implementation compatible with BokehGraph class.
"""

from enum import Enum

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

  def search(self, root, method=SearchMethod.BFS):
    collection = [root]
    marked = set(root)
    index = 0 if method == 'bfs' else -1

    while len(collection) > 0:
      v = collection.pop(index)
      print(v)
      for each in self.vertices[v]:
        if each not in marked:
          collection.append(each)
          marked.add(each)