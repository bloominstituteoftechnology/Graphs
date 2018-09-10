"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
  def __init__(self, label, component= -1):
    self.label = str(label)
    self.component = component
  def __repr__(self):
      return 'Vertex: ' + self.label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.components = 0
    def add_vertex(self, vertex, edges= ()):
      if vertex in self.vertices:
        raise Exception('Error: adding vertex that already exists')
      if not set(edges).issubset(self.vertices):
        raise Exception('Error: cannot have edge to nonexistent vertices')
      self.vertices[vertex] = set(edges)