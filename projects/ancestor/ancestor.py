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
      self.add_vertex(v1)
    
    if v2 not in self.vertices:
      self.add_vertex(v2)

    self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
  # Instantiate the Graph
  graph = Graph()

  # Added the vertices and edges between them
  for group in ancestors:
    l = list(group)
    graph.add_edge(l[1], l[0])

  # BFT 
  # Check every node in each level and find the highest level.
  # There may be muliple nodes in the highest level.
  # First-In and First-Out

  # Getting the highest node(s) logic!!!
  # We want to loop like we do for BFT.
  # We break out of it when are queue is empty and when the current node has no parents.

  # starting node = 6
  # queue = [6]
  # highest_nodes = [6]
  # index = 1
  # count = 1

  # Loop!!!
  # pop -> 6
  # queue = []
  # highest_nodes = [6, 3, 5]
  # count = 0
  # highest_nodes = [index:] = [3, 5]
  # index = 2
  # count = 2
  # queue = [3, 5]

  # pop -> 3
  # queue = [5]
  # highest_nodes = [3, 5, 1, 2]
  # count = 1
  # index = 2
  # queue = [5, 1, 2]

  # pop -> 5
  # queue = [1, 2]
  # highest_nodes = [3, 5, 1, 2, 4]
  # count = 0
  # highest_nodes = [1, 2, 4]
  # count = 3
  # index = 3
  # queue = [1, 2, 4]

  # pop -> 1
  # queue = [2, 4]
  # highest_nodes = [1, 2, 4, 10]
  # count = 2
  # index = 3
  # queue = [2, 4, 10]

  # pop -> 2
  # queue = [4, 10]
  # highest_nodes = [1, 2, 4, 10]
  # count = 1
  # index = 3
  # queue = [4, 10]

  # pop -> 4
  # queue = [10]
  # highest_nodes = [1, 2, 4, 10]
  # count = 0
  # highest_nodes = [10]
  # count = 1
  # index = 1
  # queue = [10]

  # pop -> 10
  # queue = []
  # highest_nodes = [10]
  # Done

  # Initial Set Up

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
    # Dequeue value from the queue which is the first one in line.
    node = queue.pop(0)
    bft_path.append(node)

    # Add current node's parents to highest nodes.
    highest_nodes += list(graph.vertices[node])

    # Break out of the loop when the queue is empty and when the current node has no parents.
    if not len(queue) and not graph.vertices[node]:
      break
    
    count -= 1

    # If count is 0, then modify the highest nodes list to contain all the nodes only in the highes level.
    if not count:
      highest_nodes = highest_nodes[index:]
      count = len(highest_nodes)
      index = len(highest_nodes)

    for parent in graph.vertices[node]:
      if parent not in visited:
        queue.append(parent)
        visited.add(parent)

  # print('Breadth First Traversal Path', bft_path)
  # print('Highest Nodes List', highest_nodes)

  if highest_nodes[0] == starting_node:
    return -1
  else:
    return min(highest_nodes)

# Customized input
# print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))