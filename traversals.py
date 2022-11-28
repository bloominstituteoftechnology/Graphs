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
		self.vertices = {}

	# add verts
	def add_vertex(self, vertex_id):
		self.vertices[vertex_id] = set()  # set of edges from this vert

	# add edges
	def add_edge(self, v1, v2):
		if v1 in self.vertices and v2 in self.vertices:
			self.vertices[v1].add(v2)  # add v2 as a neighbor to v1
		else:
			raise IndexError("Vertex does not exist")

	# get neighbors for a vert
	def get_neighbors(self, vertex_id):
		return self.vertices[vertex_id]

	def bft(self, starting_vertex_id):
		# Create an empty queue and enqueue the starting vertex ID
		q = Queue()
		q.enqueue(starting_vertex_id)

		# Create a Set to store visited vertices
		visited = set()

		# While the queue is not empty...
		while q.size() > 0:
			# Dequeue the first vertex
			v = q.dequeue()

			# If that vertex has not been visited...
			if v not in visited:
				# Visit it
				print(v)

				# Mark it as visited...
				visited.add(v)

				# Then add all of its neighbors to the back of the queue
				for next_vert in self.get_neighbors(v):
					q.enqueue(next_vert)

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
g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')

g.add_edge('B', 'C')
g.add_edge('B', 'A')

g.add_edge('C', 'B')

#print(g.get_neighbors('B'))
#print(g.get_neighbors('C'))

#print("----------")

#print(g.vertices)

g.bft('C')
