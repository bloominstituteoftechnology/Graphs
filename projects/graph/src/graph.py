"""
Simple graph implementation compatible with BokehGraph class.
"""
# {
# '0': {'1', '3'},
# '1': {'0'},
# '2': set(),
# '3': {'0'}
# }     


# class Edge:
#     """Edges in the adjacency list are just a destination."""
#     # Using simple classes for illustrative purposes
#     # pylint: disable=too-few-public-methods
#     def __init__(self, destination):
#         self.destination = destination


# class Vertex:
#     """Vertices have a label and a set of edges."""
#     # pylint: disable=too-few-public-methods
#     def __init__(self, label):
#         self.label = label
#         self.edges = set()


# class Graph:
#     """The graph itself is simply a set of vertices."""
#     # pylint: disable=too-few-public-methods
#     def __init__(self):
#         self.vertices = set()

class Graph:
  def __init__(self):
    self.vertices = {}
  def add_vertex(self, vertex_id):
    self.vertices[vertex_id] = set()
  def add_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
      self.vertices[v2].add(v1)
    else:
      raise IndexError("That vertex does not exist!")
  def add_directed_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
    else:
      raise IndexError("That vertex does not exist!")

# class Graph2:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.vertices:
#             self.vertices[vertex] = set()
#         else:
#             sys.exit("Vertex {} already exists.".format(vertex))

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 not in self.vertices:
#             sys.exit("No '{}' vertex!".format(vertex1))
#         elif vertex2 not in self.vertices:
#             sys.exit("No '{}' vertex!".format(vertex2))
#         else:
#             self.vertices[vertex1].add(vertex2)
#             self.vertices[vertex2].add(vertex1)