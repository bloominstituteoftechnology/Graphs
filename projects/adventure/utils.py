class Stack:
	def __init__(self):
		self.stack = []

	def length(self):
		return len(self.stack)

	def push(self, item):
		self.stack.append(item)
	def pop(self, item):
		if self.length() > 0:
			self.stack.pop(item)
		else:
			f"Stack is currently empty."
			return None

class Queue:
	def __init__(self):
		self.queue = []

	def length(self):
		return len(self.queue)

	def enqueue(self, item):
		self.queue.append(item)
	def dequeue(self, item):
		if self.length() > 0:
			self.queue.pop(0)


class Graph:
	def __init__(self, mode: str):
		self.vertices = {}
		self.edges = {}
		self.stack = Stack()
		self.queue = Queue()
		self.mode = 'Undirected'

	def set_mode(mode: str):
		self.mode = mode

	def check_mode(mode: str):
		if self.mode is mode:
			return True
		else:
			f'''This operation is for a {self.mode} Graph,
					but currently, this Graph is in {mode} mode,
					to change modes, use the setMode function
			'''
			return False

	def add_vert(self, vert):
		vertices = self.vertices
		edges = self.edges
		if vert not in vertices:
			vertices[vert] = set()
		else:
			print("This vertex already exists in the graph.")

	def add_edge(self, v1, v2):
		vertices = self.vertices
		adv = self.add_vert
		mode = self.mode
		if check_mode('Undirected'):
			if v1 and v2 not in vertices:
				vertices.adv(v1)
				vertices.adv(v2)
				vertices[v1].add(v2)
				vertices[v2].add(v1)
			elif v1 not in vertices:
				vertices.adv(v1)
				vertices[v1].add(v2)
			elif v2 not in vertices:
				vertices.add(v2)
				vertices[v1].add(v2)
		elif check_mode('Directed'):
			if v1 not in vertices:
				vertices.adv(v1)
				vertices[v1].add(v2)

	def show_verts(self):
			return self.vertices