"""
Simple graph implementation compatible with BokehGraph class.
"""



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
      self.vertices = {}
    def add_vertice(self, vertice):
      self.vertices[vertice] = set()
    def add_edge(self, vertice1, vertice2):
      if not vertice1 in self.vertices:
        print(f'Vertice {vertice1} does not exist, create missing vertice prior to creating edge.')
      elif not vertice2 in self.vertices:
        print(f'Vertice {vertice2} does not exist, create missing vertice prior to creating edge.')
      else:
        self.vertices[vertice1].add(vertice2)
        self.vertices[vertice2].add(vertice1)

graph = Graph()  # Instantiate your graph
graph.add_vertice('0')
graph.add_vertice('1')
graph.add_vertice('2')
graph.add_vertice('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '7')
print(graph.vertices)

