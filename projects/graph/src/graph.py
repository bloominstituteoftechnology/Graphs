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

    def add_edge(self, vertex1, vertex2):
    	if vertex1 not in self.vertices:
    		raise Exception(f'Vertex {vertex1} does not exist')
    	elif vertex2 not in self.vertices:
    		raise Exception(f'Vertex {vertex2} does not exist')
    	
    	self.vertices[vertex1].add(vertex2)
    	self.vertices[vertex2].add(vertex1)
    	
    	



graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
