# Stack and Queue are in util.py


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


# s = Stack()
# visited = set()

class Graph:
	def __init__(self):
		self.vertices = {}    # keys are all verts in the graph, values are sets of adj verts

	def add_vertex(self, vertex):
		"""Add a new unconnected vert"""
		self.vertices[vertex] = set()

	def add_edge(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			self.vertices[v_from].add(v_to)
		else:
			raise IndexError("nonexistent vertex")

	def is_connected(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			return v_to in self.vertices[v_from]
		else:
			raise IndexError("nonexistent vertex")

	def get_neighbors(self, v):
		return self.vertices[v]

	def bft(self, starting_vertex_id):
		q = Queue()
		visited = set()

		# Init:
		q.enqueue(starting_vertex_id)

		# While queue isn't empty
		while q.size() > 0:

			v = q.dequeue()

			if v not in visited:
				print(v)   # "Visit" the node

				visited.add(v)

				for neighbor in self.get_neighbors(v):
					q.enqueue(neighbor)

	def dft(self, starting_vertex_id):
		q = Stack()
		visited = set()

		# Init:
		q.push(starting_vertex_id)

		# While queue isn't empty
		while q.size() > 0:

			v = q.pop()

			if v not in visited:
				print(v)   # "Visit" the node

				visited.add(v)

				for neighbor in self.get_neighbors(v):
					q.push(neighbor)


	def dft_recursive(self, starting_vertex, visited=None):
		if visited is None:
			visited = set()
		print(starting_vertex)
		visited.add(starting_vertex)

		for neighbor in self.get_neighbors(starting_vertex):
			if neighbor not in visited:
				self.dft_recursive(neighbor, visited)
		

	def dft_recursive1(self, starting_vertex, visited=None):
		if visited is None:
			visited = set()
		else:
			print(starting_vertex)
			visited.add(starting_vertex)

			for value in self.vertices[starting_vertex]:
				if value not in visited:
					self.dft_recursive1(value, visited)

	def bfs(self, starting_vertex_id, target_vertex_id):
	# 	# Create an empty queue and enqueue A PATH TO the starting vertex ID
		q = Queue()
		visited = set()
		q.enqueue([starting_vertex_id])
	 # Create a Set to store visited vertices
	# 	# While the queue is not empty...
		while q.size() > 0:
	# 		# Dequeue the first PATH

			path = q.dequeue()
			v = path[-1]
	# 		# Grab the last vertex from the PATH
			if v not in visited:
				if v == target_vertex_id:
					return path
				
				visited.add(v)

				for neighbor in self.get_neighbors(v):
					new_path = path + [neighbor]
					q.enqueue(new_path)
		return None
	# 		# If that vertex has not been visited...
					# 			# Mark it as visited...
					# # CHECK IF IT'S THE TARGET
	# 			  # IF SO, RETURN PATH
						# 			# Mark it as visited...
		# then add A PATH TO its neighbors to the back of the queue
	# 			  # COPY THE PATH
	# 			  # APPEND THE NEIGHOR TO THE BACK

	def dfs(self, starting_vertex, destination_vertex):
		q = Stack()
		visited = set()
		q.push([starting_vertex])
	 # Create a Set to store visited vertices
	# 	# While the queue is not empty...
		while q.size() > 0:
	# 		# Dequeue the first PATH

			path = q.pop()
			v = path[-1]
	# 		# Grab the last vertex from the PATH
			if v not in visited:
				if v == destination_vertex:
					return path
			
				visited.add(v)

				for neighbor in self.get_neighbors(v):
					new_path = path + [neighbor]
					q.push(new_path)		

	def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
		if visited is None:
			visited = set()
		if path is None:
			path = []
		
		visited.add(starting_vertex)
		path = path + [starting_vertex]

		if starting_vertex == destination_vertex:
			return path
		else:
			for neighbor in self.get_neighbors(starting_vertex):
				if neighbor not in visited:
					new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
					if new_path:
						return new_path

	def dfs_recursive2(self, starting_vertex, destination_vertex, visited=None, path=None):
		if visited is None:
			visited = set()
		if path is None:
			path = [starting_vertex]
		
		print(starting_vertex)
		visited.add(starting_vertex)
		path += [starting_vertex]

		if starting_vertex == destination_vertex:
			return path
		else:
			for neighbor in self.get_neighbors(starting_vertex):
				if neighbor not in visited:
					new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
					if new_path:
						return new_path



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
