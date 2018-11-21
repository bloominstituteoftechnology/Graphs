"""
Simple graph implementation compatible with BokehGraph class.
"""

"""Represent a graph as a dictionary of vertices mapping labels to edges."""
class Graph:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, location):
		self.vertices[location] = set()

	def add_edge(self, location, destination):
		if location in self.vertices:
			self.vertices[location].add(destination)
		else:
			print(f'no vertex at location {location}')

	def __str__(self):
		return f'graph, vertices: {self.vertices}'

#to fit example from readme
graph = Graph()

graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')

graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '0')
graph.add_edge('3', '0')

graph.add_edge('4', '0')

print(graph)