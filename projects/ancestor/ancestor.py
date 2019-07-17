class Graph:

  def __init__(self):
    self.vertices = {}
  
  def add_vertex(self, vertex):

    if vertex not in self.vertices:
      self.vertices[vertex] = set()
  
  def add_edge(self, v1, v2):

    if v1 not in self.vertices:
      self.add_vertex(v1)
    
    if v2 not in self.vertices:
      self.add_vertex(v2)

    self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
  graph = Graph()

  for group in ancestors:
    l = list(group)
    graph.add_edge(l[1], l[0])
  queue = []
  bft_path = []
  highest_nodes = []
  visited = set()

  queue.append(starting_node)
  highest_nodes.append(starting_node)
  visited.add(starting_node)

  index = len(highest_nodes)
  count = len(highest_nodes)

  while True:
    node = queue.pop(0)
    bft_path.append(node)
    
    highest_nodes += list(graph.vertices[node])
    
    if not len(queue) and not graph.vertices[node]:
      break
    
    count -= 1

    if not count:
      highest_nodes = highest_nodes[index:]
      count = len(highest_nodes)
      index = len(highest_nodes)

    for parent in graph.vertices[node]:
      if parent not in visited:
        queue.append(parent)
        visited.add(parent)

#   print('BFT Path', bft_path)
#   print('Highest Nodes List', highest_nodes)

  if highest_nodes[0] == starting_node:
    return -1
  else:
    return min(highest_nodes)

