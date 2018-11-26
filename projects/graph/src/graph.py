"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
    	self.vertices = {}
    
    def add_vertex(self, vertex):
    	if vertex in self.vertices:
    		raise Exception('Vertice already exists')
    	else:
    		self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
    	if vertex in self.vertices:
    		self.vertices[vertex].add(edge)



graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
