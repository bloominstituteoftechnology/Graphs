from collections import deque

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
    	
    def search(self,starting_vertex, vertex):
    	if starting_vertex not in self.vertices:
    		raise Exception(f'Starting vertex {starting_vertex} does not exist')
    	if vertex not in self.vertices:
    		raise Exception(f'Vertex {vertex} does not exist')
    	
    	queue = deque()
    	queue.append(starting_vertex)

    	#keeps track if vertex is visited and its previous node
    	tally = {starting_vertex:[False,None]}


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

    	reverse_path = [vertex]
    	previous = tally[vertex][1]
    	while previous:
    		reverse_path.append(previous)
    		previous = tally[previous][1]
    	reverse_path.reverse()
    	return reverse_path

    def dfs_search(self,starting_vertex, vertex):
    	if starting_vertex not in self.vertices:
    		raise Exception(f'Starting vertex {starting_vertex} does not exist')
    	if vertex not in self.vertices:
    		raise Exception(f'Vertex {vertex} does not exist')
    	
    	stack = []
    	stack.append(starting_vertex)

    	#keeps track if vertex is visited and its previous node
    	tally = {starting_vertex:[False,None]}


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

print(graph.vertices)
print(graph.dfs_search('F', 'C'))

