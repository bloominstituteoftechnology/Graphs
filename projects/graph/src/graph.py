"""
Simple graph implementation
"""


class Graph:
	"""Represent a graph as a dictionary of vertices mapping labels to edges."""
	def __init__(self):
		self.nodes = []
		self.links = []
		pass

	def add_vertex(self,number):
		self.nodes.append(number)
		self.links.append([])
		pass
	
	def add_edge(self,number1,number2):
		self.links[self.nodes.index(number1)].append(number2)
		self.links[self.nodes.index(number2)].append(number1)
		
	def read(self):
		print ("{}   {}".format(self.nodes,self.links))
		
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.read()