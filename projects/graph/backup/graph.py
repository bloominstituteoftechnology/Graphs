"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
  """Represent a graph as a dictionary of vertices mapping labels to edges."""
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex):
    self.vertices[vertex] = set()

  def add_edge(self, vert_a, vert_b):
    if vert_a in self.vertices and vert_b in self.vertices:
      self.vertices[vert_a].add(vert_b)
    else:
      return 'exception occoured, one of the vertices is not in the Graph yet'

  def bft(self, starting_node):
    # create a queue
    q = []
    visited = set()
    # enqueue the starting node
    q.append(starting_node)
    # while the queue is not empty:
    while len(q) > 0:
      # Dequeue a node from the queue
      n = q.pop()
      # mark it as visited
      # print(f'bft visit: {n}') # <-- debugging
      visited.add(n)
      # enqueue all of it's children that have not been visited
      if self.vertices[n] != set():
        for item in self.vertices[n]:
          if item not in visited:
            q.append(item)

  def dft(self, starting_node):
    # Create a stack
    s = []
    visited = set()
    # push the starting node
    s.append(starting_node)
    # while the stack is not empty:
    while len(s) > 0:
      # pop a node from the stack
      n = s.pop(-1)
      # mark it as visited
      # print(f'dst visit: {n}') # <-- debugging
      visited.add(n)
      # push all of it's children that have not been visited
      if self.vertices[n] != set():
        for item in self.vertices[n]:
          if item not in visited:
            s.append(item)

  def dft_r(self, starting_node, visited = None):
    if visited is None:
      visited = set()
    # if the node has not been visited:
    if starting_node not in visited:
      # mark the node as visited
      # print(f'dst_r visit: {starting_node}') # <-- debugging
      visited.add(starting_node)
      # call dft_r on all children
      if self.vertices[starting_node] != set():
        for item in self.vertices[starting_node]:
          if item not in visited:
            # dft_r(child_node, visited)
            self.dft_r(item, visited)

  def bfs(self, starting_node, destination_node):
    # create a queue
    q = []
    visited = set()
    # enqueue the starting node
    q.append(starting_node)
    # while the queue is not empty:
    while len(q) > 0:
      # Dequeue a node from the queue
      n = q.pop()
      # mark it as visited
      if n == destination_node:
        return True
      visited.add(n)
      # enqueue all of it's children that have not been visited
      if self.vertices[n] != set():
        for item in self.vertices[n]:
          if item not in visited:
            q.append(item)
    return False

  def dfs(self, starting_node, destination_node):
    # Create a stack
    s = []
    visited = set()
    # push the starting node
    s.append(starting_node)
    # while the stack is not empty:
    while len(s) > 0:
      # pop a node from the stack
      n = s.pop(-1)
      # mark it as visited
      if n == destination_node:
        return True
      visited.add(n)
      # push all of it's children that have not been visited
      if self.vertices[n] != set():
        for item in self.vertices[n]:
          if item not in visited:
            s.append(item)
    return False


# q = [[1,2,3], [1,2,4]]
# visited = {1,2}

  def bfs_path(self, starting_node, destination_node):
    # create a queue
    q = []
    visited = set()
    # enqueue the starting node
    q.append([starting_node])
    # while the queue is not empty:
    while len(q) > 0:
      # Dequeue a node from the queue
      n = q.pop()
      # mark it as visited
      if n[-1] == destination_node:
        return n
      visited.add(n[-1])
      # enqueue all of it's children that have not been visited
      if self.vertices[n[-1]] != set():
        for item in self.vertices[n[-1]]:
          if item not in visited:
            q.append(n + [item])
    return False

  def dfs_path(self, starting_node, destination_node):
    # Create a stack
    s = []
    visited = set()
    # push the starting node
    s.append([starting_node])
    # while the stack is not empty:
    while len(s) > 0:
      # pop a node from the stack
      n = s.pop(-1)
      # mark it as visited
      if n[-1] == destination_node:
        return n
      visited.add(n[-1])
      # push all of it's children that have not been visited
      if self.vertices[n[-1]] != set():
        for item in self.vertices[n[-1]]:
          if item not in visited:
            s.append(n + [item])
    return False

# graph = Graph()
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('2', '3')
# graph.add_edge('1', '2')
# print(f'Graph Vertices: {graph.vertices}')
# graph.bft('0')
# graph.dft('0')
# graph.dft_r('0')
# print(graph.bfs('0', '3'))
# print(graph.bfs('0', '4'))
# print(graph.dfs('0', '3'))
# print(graph.dfs('0', '4'))
# print(graph.bfs_path('0', '3'))
# print(graph.dfs_path('0', '3'))


