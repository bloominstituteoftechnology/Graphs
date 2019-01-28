"""
Simple graph implementation
"""


class Graph:   
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex):
   if not self.vertices.get(vertex, None):
    self.vertices[vertex] = set()
    pass

  def add_edge(self, pointA, pointB):
    if not pointB in self.vertices[pointA]:
      self.vertices[pointA].add(pointB)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
print(graph.vertices)
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '3')
print(graph.vertices)