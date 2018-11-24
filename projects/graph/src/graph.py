"""
Simple graph implementation compatible with BokehGraph class.
"""

"""Represent a graph as a dictionary of vertices mapping labels to edges."""
class Graph:
	def __init__(self):
		self.vertices = {}

	#makes takes in the location paremeter and uses that to make the key
	#value on the self.vertices object, then it makes its value an empty set
	
	def add_vertex(self, location):
		self.vertices[location] = set()

	#checks if they keys are in the object
	#if it is it will add the value destination to its set list
	#sets are good because they will ever add the same item twice

	def add_edge(self, v1, v2, bi):
		if v1 and v2 in self.vertices and bi == True:
			self.vertices[v1].add(v2)
			self.vertices[v2].add(v1)
		elif v1 and v2 in self.vertices and bi == False:
			self.vertices[v1].add(v2)
		else:
			print(f'no vertex at location')

	def __str__(self):
		return f'graph, vertices: {self.vertices}'

#to fit example from readme
binary_tree = Graph()

binary_tree.add_vertex('0')
binary_tree.add_vertex('1')
binary_tree.add_vertex('2')
binary_tree.add_vertex('3')
binary_tree.add_vertex('4')
binary_tree.add_vertex('5')
binary_tree.add_vertex('6')
binary_tree.add_vertex('7')
binary_tree.add_vertex('8')
binary_tree.add_vertex('9')

binary_tree.add_edge('0', '1', False)
binary_tree.add_edge('0', '3', False)
binary_tree.add_edge('1', '2', False)
binary_tree.add_edge('2', '4', False)
binary_tree.add_edge('4', '9', False)
binary_tree.add_edge('2', '5', False)
binary_tree.add_edge('2', '4', False)
binary_tree.add_edge('3', '7', False)
binary_tree.add_edge('3', '6', False)