"""
Simple graph implementation
"""

# These may come in handy

from util import Stack, Queue

class Graph:
  """
  Represent a graph as a dictionary of vertices mapping labels to edges.
  """
  
  def __init__(self):
    self.vertices = {}
  
  def add_vertex(self, vertex):
    """
    Add a vertex to the graph.
    """
    if vertex not in self.vertices:
      self.vertices[vertex] = set()
  
  def add_edge(self, v1, v2):
    """
    Add a directed edge to the graph.
    """
    if v1 not in self.vertices:
      self.vertices[v1] = set()
    
    if v2 not in self.vertices:
      self.vertices[v2] = set()

    self.vertices[v1].add(v2)
  
  def find_connected_comps(self, path):
    """
    Finds connected vertices starting from the
    end of the path.
    """
    pass

  def bft(self, starting_vertex):
    """
    Print each vertex in breadth-first order
    beginning from starting_vertex.
    """
    pass

  def dft(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    stack = Stack()
    visited = set()
    path = []

    stack.push(starting_vertex)
    visited.add(starting_vertex)

    while stack.size():
      node = stack.pop()
      path.append(node)

      for vertex in self.vertices[node]:
        if vertex not in visited:
          stack.push(vertex)
          visited.add(vertex)
    
    return path

  def dft_recursive(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    This should be done using recursion.
    """
    pass
  
  def bfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    pass
  
  def dfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    pass

if __name__ == '__main__':
  # Instantiate your graph
  graph = Graph()
  
  graph.add_vertex(1)
  graph.add_vertex(2)
  graph.add_vertex(3)
  graph.add_vertex(4)
  graph.add_vertex(5)
  graph.add_vertex(6)
  graph.add_vertex(7)
  graph.add_edge(5, 3)
  graph.add_edge(6, 3)
  graph.add_edge(7, 1)
  graph.add_edge(4, 7)
  graph.add_edge(1, 2)
  graph.add_edge(7, 6)
  graph.add_edge(2, 4)
  graph.add_edge(3, 5)
  graph.add_edge(2, 3)
  graph.add_edge(4, 6)

  """
  Should print: {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
  """

  print("\nPrints All Vertices")
  print(f"{graph.vertices}\n")

  """
  Valid BFT paths:
  1, 2, 3, 4, 5, 6, 7
  1, 2, 3, 4, 5, 7, 6
  1, 2, 3, 4, 6, 7, 5
  1, 2, 3, 4, 6, 5, 7
  1, 2, 3, 4, 7, 6, 5
  1, 2, 3, 4, 7, 5, 6
  1, 2, 4, 3, 5, 6, 7
  1, 2, 4, 3, 5, 7, 6
  1, 2, 4, 3, 6, 7, 5
  1, 2, 4, 3, 6, 5, 7
  1, 2, 4, 3, 7, 6, 5
  1, 2, 4, 3, 7, 5, 6
  """
  
  # print("Breadth First Traversal")
  # print(f"{graph.bft(1)}\n")

  """
  Valid DFT paths:
  1, 2, 3, 5, 4, 6, 7
  1, 2, 3, 5, 4, 7, 6
  1, 2, 4, 7, 6, 3, 5
  1, 2, 4, 6, 3, 5, 7
  """
  
  print("Depth First Traversal")
  print(f"{graph.dft(1)}\n")

  """
  Valid DFT recursive paths:
  1, 2, 3, 5, 4, 6, 7
  1, 2, 3, 5, 4, 7, 6
  1, 2, 4, 7, 6, 3, 5
  1, 2, 4, 6, 3, 5, 7
  """
  
  # print("Depth First Traversal w/ Recursion")
  # print(f"{graph.dft_recursive(1)}\n")

  """
  Valid BFS path:
  [1, 2, 4, 6]
  """

  # print("Breadth First Search")
  # print(f"{graph.bfs(1, 6)}\n")

  """
  Valid DFS paths:
  [1, 2, 4, 6]
  [1, 2, 4, 7, 6]
  """
  
  # print("Depth First Search")
  # print(f"{graph.dfs(1, 6)}\n")