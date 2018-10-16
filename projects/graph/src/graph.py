"""
Simple graph implementation compatible with BokehGraph class.
"""

from collections import defaultdict


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
      self.vertices = defaultdict(set)

     def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        
     def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')

print(graph.vertices)
