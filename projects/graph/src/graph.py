#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
      self.vertices = {}

    def add_edge(self, start, end, bidirectional= True):
      if start not in self.vertices or end not in self.vertices:
        raise Exception ('Error vertices not in graph')
      # start.edges.add(end)
      self.vertices[start].add(end)
      if bidirectional:
        self.vertices[end].add(start)
        # end.edges.add(start)
        # the start exists? or end exists  raise error 
        #  if exists access the start vertex, the add(SET) if Bidrect 
        #  self.ver[start]. add 

    def add_vertex(self, vertex, edges=()):
      # if not set(edges).issubset(self,vertices):
        # raise Exception('Error: cannot have edge to nonexistant vertices')
      if vertex in self.vertices:
        raise Exception('Error: adding vertex that already exists')
      # if exists don't do anything, if not intilize it
      self.vertices[vertex] = set(edges)
    def bsf(self, vertex, edge=()):
      pass
    def dsf(self, vertex, edge()):
      pass

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# # print(graph.vertices)

# # graph.add_edge('0', '4')
# bg = BokehGraph(graph)
# bg.show()
