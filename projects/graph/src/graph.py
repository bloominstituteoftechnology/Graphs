"""
Simple graph implementation compatible with BokehGraph class.
"""



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
      self.vertices = {}
    def add_vertex(self, vertex):
      self.vertices[vertex] = set()
    def add_edge(self, vertex1, vertex2):
      if not vertex1 in self.vertices:
        raise IndexError(f'vertex {vertex1} does not exist, create missing vertex prior to creating edge.')
      elif not vertex2 in self.vertices:
        raise IndexError(f'vertex {vertex2} does not exist, create missing vertex prior to creating edge.')
      else:
        self.vertices[vertex1].add(vertex2)
        self.vertices[vertex2].add(vertex1)







        

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('0', '7')
# print(graph.vertices)



