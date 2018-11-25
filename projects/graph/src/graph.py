"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
	def __init__(self, vertex_id, x=None, y=None, value=None, color='white'):
		self.id = int(vertex_id)
		self.x = x
		self.y = y
		self.value = value
		self.color = color
		self.edges = set()
		if self.x is None:
			self.x = self.id
		if self.y is None:
			self.y = self.id
		if self.value is None:
			self.value = self.id
	def __str__(self):
		return f'edges: {self.edges}'

"""Represent a graph as a dictionary of vertices mapping labels to edges."""
class Graph:
	def __init__(self):
		self.vertices = {}
	
	def add_vertex(self, vertex_id):
		self.vertices[vertex_id] = Vertex(vertex_id)

	def add_edge(self, v1, v2, bi):
		check_one = False
		check_two = False

		for i in self.vertices: 
			if self.vertices[i].id == v1:
				check_one = True
			if self.vertices[i].id == v2:
				check_two = True

		if check_one and check_two and bi == True:
			self.vertices[v1].edges.add(v2)
			self.vertices[v2].edges.add(v1)

		elif check_one and check_two == True and bi == False:
			self.vertices[v1].edges.add(v2)
		else:
			print(f'no vertex at location v1:, {v1}, v2: {v2}')

	def depth_first(self, node, node_list, target):
		node_list.append(node)
		if node == target:
			return print(f'node: {node} was found in tree')

		for child_node in self.vertices[node]:
			if child_node not in node_list:
				self.depth_first(child_node, node_list, target)

	def breath_first(self, node, target):

		list_n = []
		list_n.append(node)
		checked = []
		while len(list_n) > 0:
			n = list_n.pop(0)
			if n not in checked:
				print(n)
				if n == target:
					print(f'node: {target} was found in tree')
					return
				checked.append(n)
				for next_node in self.vertices[n]:
					list_n.append(next_node)

	def __str__(self):
		return f'graph, vertices: {self.vertices}'

#to fit example from readme
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
binary_tree.add_vertex(9)

binary_tree.add_edge(0, 1, True)
binary_tree.add_edge(0, 3, True)
binary_tree.add_edge(1, 2, True)
binary_tree.add_edge(2, 4, True)
binary_tree.add_edge(4, 9, True)
binary_tree.add_edge(2, 5, True)
binary_tree.add_edge(2, 4, True)
binary_tree.add_edge(3, 7, True)
binary_tree.add_edge(3, 6, True)

# print(binary_tree.vertices)

#examples
# binary_tree.depth_first('0', [], '9')
# binary_tree.breath_first('0', '7')


