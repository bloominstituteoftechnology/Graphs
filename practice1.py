




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

  def bft(self, starting_vertex_id):
    # Create an empty Queue and add starting vertex to it
    queue = [] # FIFO
    # This will keep track of all next_to_visit_vertices
    queue.append(starting_vertex_id)
    # Create an empty set to keep track of visited vertices
    visited = set()
    # While the queue is not empty
    while len(queue) > 0:
      #dequeue a vertex off the queue
      current_vertex = queue.pop(0)
      # if vertex not in visited vertices
      if current_vertex not in visited:      
        # Print it
        print(current_vertex)
        # Add the vertex to our visited set
        visited.add(current_vertex)
        # ***Add all neighbors to the queue ****
        for neighbor in self.get_neighbors(current_vertex):
          # Add all the neighbor to the queue so that you can..
          queue.append(neighbor)

  def dft(self, starting_vertex_id):    
    # Create an empty stack and add starting vertex to it
    stack = [] # LIFO
    # This will keep track of all next_to_visit_vertices
    stack.append(starting_vertex_id)
    # Create an empty set to keep track of visited vertices
    visited = set()
    # While the stack is not empty
    while len(stack) > 0:
      # remove stack a vertex off the stack
      current_vertex = stack.pop()
      # if vertex not in visited vertices
      if current_vertex not in visited:      
        # Print it
        print(current_vertex)
        # Add the vertex to our visited set
        visited.add(current_vertex)
        # ***Add all neighbors to the stack ****
        for neighbor in self.get_neighbors(current_vertex):
          # Add all the neighbor to the stack so that you can..
          stack.append(neighbor)        








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
our_graph.dft(1)
print(our_graph.vertices)

