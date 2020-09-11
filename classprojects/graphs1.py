"""
class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.next = None
"""
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
​
class Queue():
    def __init__(self):
        self.queue = []
​
    def enqueue(self, value):
        self.queue.append(value)
​
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
​
    def size(self):
        return len(self.queue)
​
class Node:  # Graph Node
	def __init__(self, value):
		self.value = value
		self.neighbors = []  # Adjecency List representation of a graph
​
	def __repr__(self):
		return f'Node({repr(self.value)})'
​
def bft(node):
	# Create a queue to hold nodes to visit
	to_visit = Queue()
​
	# Create a set to hold visited nodes
	visited = set()
​
	# Initalize: add the starting node to the queue
	to_visit.enqueue(node)
​
	# While queue not empty:
	while to_visit.size() > 0:
		# dequeue first entry
		v = to_visit.dequeue()
​
		# if not visited:
		if v not in visited:
			# Visit the node (print it out)
			print(v)
​
			# Add it to the visited set
			visited.add(v)
​
			# enqueue all its neighbors
			for n in v.neighbors:
				#print(f"Adding: {n}")
				to_visit.enqueue(n)
​
def dft(node):
	# Create a stack to hold nodes to visit
	to_visit = Stack()
​
	# Create a set to hold visited nodes
	visited = set()
​
	# Initalize: add the starting node to the queue
	to_visit.push(node)
​
	# While queue not empty:
	while to_visit.size() > 0:
		# dequeue first entry
		v = to_visit.pop()
​
		# if not visited:
		if v not in visited:
			# Visit the node (print it out)
			print(v)
​
			# Add it to the visited set
			visited.add(v)
​
			# enqueue all its neighbors
			for n in v.neighbors:
				#print(f"Adding: {n}")
				to_visit.push(n)
​
"""
def dft_recursive(node):
	# Broken pseudocode
	for n in node.neighbors:
		dft_recursive(n)
"""
​
def bfs(starting_vertex, target_vertex):
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
​
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
​
a.neighbors.append(c)
a.neighbors.append(b)
​
b.neighbors.append(b)
b.neighbors.append(c)
b.neighbors.append(d)
​
c.neighbors.append(b)
​
bft(b)
​
​
