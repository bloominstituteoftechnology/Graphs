class Vertex:
	def __init__(self, vertex_id):
		self.vertex_id = int(vertex_id)
		self.edges = set()
	def __str__(self):
		return f'edges: {self.edges}'

class Graph:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, vertex_id):
		self.vertices[vertex_id] = Vertex(vertex_id)

	def add_edge(self, v1, v2, bi):
		check_one = False
		check_two = False

		for i in self.vertices: 
			if self.vertices[i].vertex_id == v1:
				check_one = True
			if self.vertices[i].vertex_id == v2:
				check_two = True

		if check_one and check_two and bi == True:
			self.vertices[v1].edges.add(v2)
			self.vertices[v2].edges.add(v1)

		elif check_one and check_two == True and bi == False:
			self.vertices[v1].edges.add(v2)
		else:
			print(f'no vertex at location v1:, {v1}, v2: {v2}')

	def bft(self, node):

		q = []
		q.append([node])
		bft_list = []
		checked = []

		while len(q) > 0:

			if len(q) > 0:
				next_in_line = q.pop(0)

			n = next_in_line[0]

			if n not in checked:

				bft_list.append(n)
				checked.append(n)
				for i in self.vertices[n].edges:
					q.append([i])

		return bft_list

	def dft(self, node):

		s = []
		s.append([node])
		dft_list = []
		checked = []

		while len(s) > 0:

			if len(s) > 0:
				next_in_line = s.pop()
				
			n = next_in_line[0]

			if n not in checked:

				dft_list.append(n)
				checked.append(n)
				for i in self.vertices[n].edges:
					s.append([i])

		return dft_list

	def __str__(self):
		return f'graph, vertices: {self.vertices}'

binary_tree = Graph()
binary_tree.add_vertex(0)
binary_tree.add_vertex(1)
binary_tree.add_vertex(2)
binary_tree.add_vertex(3)
binary_tree.add_vertex(4)
binary_tree.add_vertex(5)
binary_tree.add_vertex(6)
binary_tree.add_vertex(7)
binary_tree.add_vertex(8)

binary_tree.add_edge(0, 1, False)
binary_tree.add_edge(0, 3, False)
binary_tree.add_edge(1, 2, False)
binary_tree.add_edge(3, 6, False)
binary_tree.add_edge(3, 7, False)
binary_tree.add_edge(2, 4, False)
binary_tree.add_edge(2, 5, False)
binary_tree.add_edge(4, 8, False)

print(binary_tree.bft(0))
print(binary_tree.dft(0))