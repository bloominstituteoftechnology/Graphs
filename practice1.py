




class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex_id):
    self.vertices[vertex_id] = set()
  
  def add_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
    else:
      print("Error vertices not found")  

  def get_neighbors(self, vertex_id):
    return self.vertices[vertex_id]

    



our_graph = Graph()  
our_graph.add_vertex(1)
our_graph.add_vertex(2)
our_graph.add_vertex(3)
our_graph.add_vertex(4)
our_graph.add_vertex(5)
our_graph.add_vertex(6)
our_graph.add_vertex(7)
our_graph.add_edge(1,2)
our_graph.add_edge(2,3)
our_graph.add_edge(2,4)
our_graph.add_edge(3,5)
our_graph.add_edge(4,6)
our_graph.add_edge(4,7)
our_graph.add_edge(5,3)
our_graph.add_edge(7,1)
our_graph.add_edge(7,6)
our_graph.add_edge(6,3)

print(our_graph.vertices)

