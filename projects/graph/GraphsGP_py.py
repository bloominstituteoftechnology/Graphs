class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None
    # reference to the tail of the list
    self.tail = None

  def add_to_tail(self, value):
    # wrap the input value in a node
    new_node = Node(value, None)
    # check if there is no head (i.e., the list is empty)
    if not self.head:
      # if the list is initially empty, set both head and tail to the new node
      self.head = new_node
      self.tail = new_node
    # we have a non-empty list, add the new node to the tail
    else:
      # set the current tail's next reference to our new node
      self.tail.set_next(new_node)
      # set the list's tail reference to the new node
      self.tail = new_node

  def remove_head(self):
    # return None if there is no head (i.e. the list is empty)
    if not self.head:
      return None
    # if head has no next, then we have a single element in our list
    if not self.head.get_next():
      # get a reference to the head
      head = self.head
      # delete the list's head reference
      self.head = None
      # also make sure the tail reference doesn't refer to anything
      self.tail = None
      # return the value
      return head.get_value()
    # otherwise we have more than one element in our list
    value = self.head.get_value()
    # set the head reference to the current head's next node in the list
    self.head = self.head.get_next()
    return value

  def contains(self, value):
    if not self.head:
      return False

    # Recursive solution
    # def search(node):
    #   if node.get_value() == value:
    #     return True
    #   if not node.get_next():
    #     return False
    #   return search(node.get_next())
    # return search(self.head)
  
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def get_max(self):
    if not self.head:
      return None
    # reference to the largest value we've seen so far
    max_value = self.head.get_value()
    # reference to our current node as we traverse the list
    current = self.head.get_next()
    # check to see if we're still at a valid list node
    while current:
      # check to see if the current value is greater than the max_value
      if current.get_value() > max_value:
        # if so, update our max_value variable
        max_value = current.get_value()
      # update the current node to the next node in the list
      current = current.get_next()
    return max_value


class Queue:
  def __init__(self):
    # counter to keep track of the number of elements in our queue
    self.size = 0
    # we'll use our LinkedList implementation to build the queue
    self.storage = LinkedList()

  def enqueue(self, item):
    # add the item to the linked list 
    self.storage.add_to_tail(item)
    # increment our size counter
    self.size += 1
  
  def dequeue(self):
    # decrement our size counter
    if self.size > 0:
      self.size -= 1
    # remove the head of the linked list and return it
    return self.storage.remove_head()

  def len(self):
    return self.size

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def bft(self, starting_vertex_id):
			# Create an empty queue 
      queue = Queue()
			# enqueue the starting vertex ID 
      queue.enqueue(starting_vertex_id)
			# Create a set to store the visited vertices
      visited = set()
			# While the queue is not empty...
      while queue.size > 0:
				# Dequeue the first vertex
        vertex = queue.dequeue()
				# If that vertex has not been visited...
        if vertex not in visited:
					# Mark it as visited
          print(vertex)
          visited.add(vertex)
					# Then add all of it's neighbors to the back of the queue
          for next_vertex in self.vertices[vertex]:
            queue.enqueue(next_vertex)

    def dft(self, starting_vertex_id):
			 # Create an empty stack and push the starting vertex ID
       stack = Stack()
			 # enqueue the starting vertex ID 
       stack.push(starting_vertex_id)
			 # Create a Set to store visited vertices
       visited = set()
			 # While the stack is not empty...
       while stack.size() > 0:
			 		# Pop the first vertex
          vertex = stack.pop()
					# If that vertex has not been visited...	
          if vertex not in visited:
							 # Mark it as visited...
               print(vertex)
               visited.add(vertex)
							 # Then add all of its neighbors to the top of the stack
               for next_vertex in self.vertices[vertex]:
                 stack.push(next_vertex)
		
    def bfs(self, starting_vertex_id, target_vertex_id):
				# Create an empty queue and enqueue A PATH TO the starting vertex ID
				# Create a Set to store visited vertices
				# While the queue is not empty...
						# Dequeue the first PATH
						# Grab the last vertex from the PATH
						# If that vertex has not been visited...
								# CHECK IF IT'S THE TARGET
									# IF SO, RETURN PATH
								# Mark it as visited...
								# Then add A PATH TO its neighbors to the back of the queue
									# COPY THE PATH
									# APPEND THE NEIGHOR TO THE BACK
      return

graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_edge('1', '2')
graph.add_edge('2', '3')
graph.add_edge('2', '4')
graph.add_edge('3', '5')
graph.add_edge('4', '6')
graph.add_edge('4', '7')
graph.add_edge('5', '3')
graph.add_edge('6', '3')
graph.add_edge('7', '1')
graph.add_edge('7', '6')
print(graph.vertices)

print("A breadth first traversal starting at vertex 1:")
graph.bft('1')
print("A depth first traversal starting at vertex 1:")
graph.dft('1')