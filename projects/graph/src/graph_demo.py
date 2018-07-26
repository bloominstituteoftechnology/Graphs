#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from random import sample
from graph import Graph
from draw import BokehGraph

def main():
  graph = Graph()

  vertices = set()
  for v in range(num_vertices):
    graph.add_vertex(v)
    vertices.add(v)

  edges = set()
  while len(edges) < num_edges:
    pair = sample(vertices, 2)
    edge = (min(pair), max(pair))
    if edge not in edges:
      graph.add_edge(edge[0], edge[1])
      edges.add(edge)

  bg = BokehGraph(graph)
  bg.show()

if __name__ == '__main__':
  num_vertices = 4
  num_edges = 6
  if len(argv) == 3:
    num_vertices = int(argv[1])
    num_edges = min(int(argv[2]), int(num_vertices*(num_vertices-1)/2))
  main()
