#!/usr/bin/python

from random import choice

"""
Simple graph implementation compatible with BokehGraph class.
"""
class Edge:
  def __init__(self, destination, weight=1):
    self.destination = destination
    self.weight = weight

class Vertex:
  def __init__(self, value='V', color='#000000'):
    self.value = value
    self.edges = set()
    self.color = color

class Graph:
  def __init__(self):
    self.vertices = {}

  def __repr__(self):
      return str(self.vertices)

  def add_vertex(self, vertex, color='#000000'):
    if vertex in self.vertices:
      raise ValueError('Duplicate vertex name')
    self.vertices[vertex] = Vertex(vertex, color)
  
  def add_edge(self, start, end, bidirectional=True):
    if start not in self.vertices or end not in self.vertices:
      raise Exception("Error, vertices not in graph!")
    self.vertices[start].edges.add(end)
    if bidirectional:
      self.vertices[end].edges.add(start)

  def depth_first_search(self):
    visited = set()
    for vertex in self.vertices:
      stack = []
      stack.append(self.vertices[vertex])
      color = get_random_color()
      print('start')
      while len(stack) > 0:
        v = stack.pop()
        print('pop from stack {} {}'.format(v.value, v.color))
        if v not in visited:
          print('Not visted {} {}'.format(v.value, v.color))
          v.color = color
          visited.add(v)
          print('Visted change color {} {}'.format(v.value, v.color))
          for edge in v.edges:
            stack.append(self.vertices[edge])
        else:
          print('Visted {} {}'.format(v.value, v.color))

def get_random_color():
  color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
  return color


  