from collections import deque
from enum import Enum

"""
Simple graph implementation
"""
class Algorithm(Enum):
	BREADTH = 0
	DEPTH = 1

#Implement queue class using deque class
class Queue(deque):
	def __init__(self):
		super().__init__()

	def pop(self):
		return super().popleft()

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
    	self.vertices = {}
    
    def add_vertex(self, vertex):
    	if vertex in self.vertices:
    		raise Exception('Vertice already exists')
    	else:
    		self.vertices[vertex] = set()

    #takes an optional bool argument for bidirectional
    def add_edge(self, vertex1, vertex2, bidirectional = True):
    	if vertex1 not in self.vertices:
    		raise Exception(f'Vertex {vertex1} does not exist')
    	elif vertex2 not in self.vertices:
    		raise Exception(f'Vertex {vertex2} does not exist')
    	
    	if bidirectional:
    		self.vertices[vertex1].add(vertex2)
    		self.vertices[vertex2].add(vertex1)
    	else:
    		self.vertices[vertex1].add(vertex2)

    #PART 2 and 3 - BFT and DFT
    #Takes starting_vertex and algorithm_type as arguments.
    #Algorithm_type expects an Algorithm ENUM to be used.
    def traversal(self, starting_vertex, algorithm_type):
    	# checks to make sure starting vertex is valid
    	if starting_vertex not in self.vertices:
    		raise Exception(f'Starting vertex {starting_vertex} does not exist')

    	# Uses either a queue or stack for BFT or DFT respectively
    	if algorithm_type.name == "BREADTH":
    		print("Breadth First Traversal:")
    		storage = Queue()
    	elif algorithm_type.name == "DEPTH":
    		print("Depth First Traversal:")
    		storage = []

    	storage.append(starting_vertex)
    	visited = set()
    	
    	result = []
    	while storage:
    		current_vertex = storage.pop()
    		neighbors = self.vertices[current_vertex]

    		for neighbor in neighbors:
    			if neighbor not in visited and neighbor not in storage:
    				storage.append(neighbor)

    		visited.add(current_vertex)
    		result.append(current_vertex)

    	return ', '.join(result)


    # PART 3.5: Recursive implementation
    def _dft_recursive_helper(self, vertex, result, visited = set()):

    	visited.add(vertex)
    	result.append(vertex)
    	neighbors = self.vertices[vertex]
    	for neighbor in neighbors:
    		if neighbor not in visited:
    			self._dft_recursive_helper(neighbor, result, visited)

    def dft_recursive(self, vertex):
    	result = []
    	print("Recursive Depth First Traversal:")
    	self._dft_recursive_helper(vertex, result)
    	return " ,".join(result)


    # PART 4 and 5
    def search(self, starting_vertex, vertex, algorithm_type):
    	if starting_vertex not in self.vertices:
    		raise Exception(f'Starting vertex {starting_vertex} does not exist')
    	if vertex not in self.vertices:
    		raise Exception(f'Vertex {vertex} does not exist')	

    	# Uses either a queue or stack for BFT or DFT respectively
    	if algorithm_type.name == "BREADTH":
    		print("Breadth First Search:")
    		storage = Queue()
    	elif algorithm_type.name == "DEPTH":
    		print("Depth First Search:")
    		storage = []

    	storage.append(starting_vertex)
    	record = {starting_vertex: None}
    	
    	result = []
    	while storage:
    		current_vertex = storage.pop()
    		if current_vertex == vertex:
    			break

    		neighbors = self.vertices[current_vertex]

    		for neighbor in neighbors:
    			if neighbor not in record and neighbor not in storage:
    				storage.append(neighbor)
    				record[neighbor] = current_vertex

    	return self._get_path(record, vertex)

    def _get_path(self,tally, vertex):
    	reverse_path = [vertex]
    	previous = tally[vertex]
    	while previous:
    		reverse_path.append(previous)
    		previous = tally[previous]
    	reverse_path.reverse()
    	return ", ".join(reverse_path)
 


graph = Graph()  # Instantiate your graph
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_edge('A', 'B')
graph.add_edge('A', 'F')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('B', 'F')
graph.add_edge('C', 'E')
graph.add_edge('A', 'C')

print(graph.traversal("F",Algorithm.BREADTH))
print(graph.traversal("F",Algorithm.DEPTH))
print(graph.dft_recursive('F') + "\n")
print(graph.search("F", "C",Algorithm.BREADTH))
print(graph.search("F", "C",Algorithm.DEPTH))
