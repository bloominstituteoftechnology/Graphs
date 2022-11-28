
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

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
	def __init__(self):
		self.vertices = {}    # keys are all verts in the graph, values are sets of adj verts

	def add_vertex(self, vertex):
		"""Add a new unconnected vert"""
		self.vertices[vertex] = set()

	def add_edge(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			self.vertices[v_from].add(v_to)
		else:
			raise IndexError("nonexistent vertex")

	def is_connected(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			return v_to in self.vertices[v_from]
		else:
			raise IndexError("nonexistent vertex")

	def get_neighbors2(self, v):
		return self.vertices[v]


def earliest_ancestor(ancestors, starting_node):
    pass
    #if acyclic either bfs and dfs
    #take a starting node and see which node is the furthest away
    #count of the steps taken
    #if count is the same for two items return the smaller value
    #return the length of every list
    #assign value of the last index
    #dictionary that coded the child from the parent

def get_neighbors(ancestors, n): #test_anscestors = []
    neighbors = []

    for a in ancestors:
        if a[1] == n:
            neighbors.append(a[0])
    return neighbors


def bfs(self, starting_vertex_id, target_vertex_id):
# 	# Create an empty queue and enqueue A PATH TO the starting vertex ID
    q = Queue()
    visited = set()
    q.enqueue([starting_vertex_id])
    # Create a Set to store visited vertices
# 	# While the queue is not empty...
    while q.size() > 0:
# 		# Dequeue the first PATH

        path = q.dequeue()
        v = path[-1]
# 		# Grab the last vertex from the PATH
        if v not in visited:
            if v == target_vertex_id:
                return path
            
            visited.add(v)

            for neighbor in self.get_neighbors(v):
                new_path = path + [neighbor]
                q.enqueue(new_path)
    return None

def dft(self, starting_vertex_id):
    q = Stack()
    visited = set()

    # Init:
    q.push(starting_vertex_id)

    # While queue isn't empty
    while q.size() > 0:

        v = q.pop()

        if v not in visited:
            print(v)   # "Visit" the node

            visited.add(v)

            for neighbor in self.get_neighbors(v):
                q.push(neighbor)
