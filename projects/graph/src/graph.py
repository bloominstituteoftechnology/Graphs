#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
class Graph:
  def __init__(self):
    self.vertices = {}

  def __repr__(self):
      return str(self.vertices)

  def add_vertex(self, vertex):
    if vertex in self.vertices:
      raise ValueError('Duplicate vertex name')
    self.vertices[vertex] = set()
  
  def add_edge(self, start, end, bidirectional=True):
    if start not in self.vertices or end not in self.vertices:
      raise Exception("Error, vertices not in graph!")
    self.vertices[start].add(end)
    if bidirectional:
      self.vertices[end].add(start)


graph = Graph()  # Instantiate your graph
print(graph)

graph.add_vertex('0')
print(graph)

graph.add_vertex('1')
print(graph)

graph.add_vertex('2')
print(graph)

graph.add_vertex('3')
print(graph)

graph.add_edge('0', '1')
print(graph)

graph.add_edge('0', '3')
print(graph)

# graph.add_vertex('3')
# print(graph)

graph.add_edge('2', '4')
print(graph)
