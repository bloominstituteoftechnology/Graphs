from collections import deque
from enum import Enum

"""
Simple graph implementation compatible with BokehGraph class.
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

    #PART 2 - BFT
    #Takes starting_vertex and algorithm_type as arguments.
    #Algorithm_type expects an Algorithm ENUM to be used.
    def traversal(self, starting_vertex, algorithm_type):
    	if starting_vertex not in self.vertices:
    		raise Exception(f'Starting vertex {starting_vertex} does not exist')

    	if algorithm_type.name == "BREADTH":
    		print("Breadth First Traversal:")
    		storage = Queue()
    	elif algorithm_type.name == "DEPTH":
    		print("Depth First Traversal:")
    		storage = []
    	else:
    		raise Exception(f'algorithm_type is not a valid algorithm type. Check Algorithm enum for valid options.')

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

    def dft_recursive(self, vertex, visited = set()):

    	visited.add(vertex)
    	print(vertex)
    	neighbors = self.vertices[vertex]
    	for neighbor in neighbors:
    		if neighbor not in visited:
    			self.dft_recursive(neighbor,visited)




    def search(self,starting_vertex, vertex, option = 0):
    	if starting_vertex not in self.vertices:
    		raise Exception(f'Starting vertex {starting_vertex} does not exist')
    	if vertex not in self.vertices:
    		raise Exception(f'Vertex {vertex} does not exist')
    	
    	tally = {starting_vertex:[False,None]}

    	if option == 0:
    		print("BFS chosen")
    		self.bfs_search(starting_vertex, vertex, tally)
    	else:
    		print("DFS chosen")
    		self.dfs_search(starting_vertex, vertex, tally)

    	return self._get_path(tally, vertex)

    def bfs_search(self,starting_vertex, vertex, tally):
    	
    	queue = deque()
    	queue.append(starting_vertex)

    	#keeps track if vertex is visited and its previous node
    	while queue:
    		#dequeue vertex
    		current_vertex = queue.popleft()
    		#stops while loop if vertex has been found
    		if current_vertex == vertex:
    			break
    		#gets neighbors of vertex and adds it to queue
    		neighbors = self.vertices[current_vertex]

    		#update tally to include neighbors keeping track of prev node
    		for neighbor in neighbors:
    			if neighbor not in tally:
    				tally[neighbor] = [False, current_vertex]
    				queue.append(neighbor)
    		#mark vertex as visited
    		tally[current_vertex][0] = True

    def dfs_search(self,starting_vertex, vertex, tally):
    	stack = []
    	stack.append(starting_vertex)

    	#keeps track if vertex is visited and its previous node
    	while stack:
    		#dequeue vertex
    		current_vertex = stack.pop()
    		#stops while loop if vertex has been found
    		if current_vertex == vertex:
    			break
    		#gets neighbors of vertex and adds it to queue
    		neighbors = self.vertices[current_vertex]

    		#update tally to include neighbors keeping track of prev node
    		for neighbor in neighbors:
    			if neighbor not in tally:
    				tally[neighbor] = [False, current_vertex]
    				stack.append(neighbor)
    		#mark vertex as visited
    		tally[current_vertex][0] = True

    def _get_path(self,tally, vertex):
    	reverse_path = [vertex]
    	previous = tally[vertex][1]
    	while previous:
    		reverse_path.append(previous)
    		previous = tally[previous][1]
    	reverse_path.reverse()
    	return reverse_path















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

# print(graph.traversal("F",Algorithm.BREADTH))
print(graph.traversal("F",Algorithm.DEPTH))
graph.dft_recursive('F')
