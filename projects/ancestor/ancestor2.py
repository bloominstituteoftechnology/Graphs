import sys 
sys.path.append('../')

from graph.util import Stack, Queue

class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertices(self, vertex_id):
    if vertex_id not in self.vertices:
      self.vertices[vertex_id] = set()

  def add_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
    else:
      print('Vertex not found')  

  def get_neighbors(self, vertex_id):
    return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
  graph = Graph()
  ancestors_list = {}
  #loop through the ancestors tuples of list
  for ancestor in ancestors:
    parent = ancestor[0]
    child = ancestor[1]
    if child not in ancestors_list:
      ancestors_list[child] = set()
    if parent not in ancestors_list:
      ancestors_list[parent] = set()
    ancestors_list[child].add(parent)
  print(f'Ancestors_list {ancestors_list}')
  s = Stack()
  s.push([starting_node])
  print(f"Starting_node {starting_node}")
  longest_path_length = 1
  earliest_ancestor = -1
  visited = set()

  while s.size() > 0:
    current_path = s.pop()
    current_vertex = current_path[-1]
    print(f"currentPath: {current_path} current_vertex: {current_vertex}")
    if current_vertex not in visited:
      visited.add(current_vertex)
      print(f"current_path:{current_path} current_path_length:{len(current_path)}")
      print(f"longest_path_length:{longest_path_length}")
      print('Next iteration')

      if len(current_path) > longest_path_length:
        longest_path_length = len(current_path)
        earliest_ancestor = current_vertex

      for neighbor in ancestors_list[current_vertex]:          
          new_path = list(current_path)
          new_path.append(neighbor)
          s.push(new_path)

  return earliest_ancestor

  


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
print(earliest_ancestor(test_ancestors, 4))
print(earliest_ancestor(test_ancestors, 5))        
print(earliest_ancestor(test_ancestors, 7))        
print(earliest_ancestor(test_ancestors, 8))        
print(earliest_ancestor(test_ancestors, 9))        
print(earliest_ancestor(test_ancestors, 10))
print(earliest_ancestor(test_ancestors, 11))