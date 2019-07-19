class Graph:
	def __init__(self, mode: str):
		self.vertices = {}
		self.edges = {}
		self.stack = Stack()
		self.queue = Queue()
		self.mode = 'Undirected'

		def setMode(mode: str):
			self.mode = mode

		def checkMode(mode: str):
			if self.mode is str:
				return True
			else:
				print("This is an operation for an {}")
				return False

		def addVert(self, vert):
			vertices = self.vertices
			edges = self.edges
			if vert not in vertices:
				vertices[vert] = set()
			else:
				print("This vertex already exists in the graph.")

		def addEdge(self, v1, v2):
			vertices = self.vertices
			adv = self.addVert
			mode = self.mode
			if checkMode('Undirected'):
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
			elif checkMode('Directed'):
				if v1 not in vertices:
					vertices.adv(v1)
					vertices[v1].add(v2)

