




class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex_id):
    self.vertices[vertex_id] = set()
  
  def add_edge(self, v1, v2):
    self.vertices[v1].add(v2)


our_graph = Graph()  
our_graph.add_vertex(1)
our_graph.add_vertex(2)
our_graph.add_vertex(3)
our_graph.add_edge(1,2)
our_graph.add_edge(1,3)
our_graph.add_edge(1,4)

print(our_graph.vertices)

