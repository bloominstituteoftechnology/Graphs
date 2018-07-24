#!/usr/bin/python
from collections import defaultdict

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
  """Vertices have a 'label' and a set of edges"""
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
      retun str(self.label)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        pass  # TODO
