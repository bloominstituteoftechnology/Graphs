"""
Simple graph implementation
"""
from collections import deque

class Stack:
  def __init__(self):
    self.__storage = []

  def isEmpty(self):
    return len(self.__storage) == 0

  def push(self,p):
    self.__storage.append(p)

  def pop(self):
    return self.__storage.pop()

class Vertex:
  def __init__(self, vertex):
    self.value = vertex
    self.visited = False
    self.edges = {}

  def __repr__(self):
    return str([self.edges[edge].value for edge in self.edges])
 

class Graph:   
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex):
   if not self.vertices.get(vertex, None):
    self.vertices[vertex] = Vertex(vertex)
    pass

  def add_edge(self, pointA, pointB):
    self.add_vertex(pointA)
    self.add_vertex(pointB)

    if not pointB in self.vertices[pointA].edges:
      self.vertices[pointA].edges[pointB] = self.vertices[pointB]
    if not pointA in self.vertices[pointB].edges:
      self.vertices[pointB].edges[pointA] = self.vertices[pointA]
  
  def bft(self, starting_node):
    queque = deque([])
    visited = []
    queque.appendleft(self.vertices[starting_node])
    while len(queque) > 0:
      current_node = queque.popleft()
      current_node.visited = True
      visited.append(current_node.value)
      for node in current_node.edges.values():
        if not node.visited:
          queque.appendleft(node)    
      print(current_node.value)
  
  def bfs(self, starting_node, target):
    queque = deque([])
    queque.appendleft(self.vertices[starting_node])
    visited = []
    while len(queque) > 0:
      current_node = queque.popleft()
      current_node.visited = True
      visited.append(current_node.value)
      if current_node.value == target:
        print(visited)
        return
      else:        
        for node in current_node.edges.values():
          if not node.visited:
            queque.appendleft(node)
  def dfs(self, current_node, target):
    node = self.vertices[current_node]
    visited = []
    s = Stack()
    s.push(node)
    while not s.isEmpty():
      current_node = s.pop()
      current_node.visited = True
      visited.append(current_node.value)
      if current_node.value == target:
        print(visited)
        return
      for node in current_node.edges.values():
        if not node.visited:
          s.push(node)
    

  def dft(self, current_node):
    
    node = self.vertices[current_node]

    print(node.value)
    node.visited = True
    for key, child in node.edges.items():
      if not child.visited:
        self.dft(key)
  
  def dft_s(self, current_node):
    s = Stack()
    node = self.vertices[current_node]
    s.push(node)
    while not s.isEmpty():
      current_node = s.pop()
      current_node.visited = True
      print(current_node.value)
      for node in current_node.edges.values():
        if not node.visited:
          s.push(node)
  





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
graph.add_edge('0', '4')
print(graph.vertices)
graph.dfs("0", "4")