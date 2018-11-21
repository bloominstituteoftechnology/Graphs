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

	#checks if they key is in the object
	#if it is it will add the value destination to its set list
	#sets are good because they will ever add the same item twice

	def add_edge(self, location, destination):
		if location in self.vertices:
			self.vertices[location].add(destination)
		else:
			print(f'no vertex at location {location}')

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

binary_tree.add_edge('0', '1')
binary_tree.add_edge('0', '2')

binary_tree.add_edge('1', '3')
binary_tree.add_edge('1', '4')

binary_tree.add_edge('2', '5')
binary_tree.add_edge('2', '6')