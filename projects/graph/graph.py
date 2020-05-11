"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
	"""Represent a graph as a dictionary of vertices mapping labels to edges."""

	def __init__(self):
		self.vertices = {}

	def add_vertex(self, vertex_id):
		self.vertices[vertex_id] = set()

	def add_edge(self, v1, v2):
		if v1 in self.vertices and v2 in self.vertices:
			self.vertices[v1].add(v2)

	def get_neighbors(self, vertex_id):
		return self.vertices[vertex_id]

	def bft(self, starting_vertex):
		# print(f'Graph: {self.vertices}')
		# print('starting vertex', starting_vertex)
		q = Queue()
		q.enqueue(starting_vertex)
		# print(f'Enqueueing starting vertex: {starting_vertex}')
		visited = set()
		while q.size() > 0:
			v = q.dequeue()
			if v not in visited:
				# print(f'Currently visiting {v}')
				# print(f'{v} is not in {visited}')
				visited.add(v)
				# print(f'Added {v} to visited set')
				# print(f'Visited: {visited}')
				for next_vert in self.get_neighbors(v):
					# print(f'Neighbors of {v}: {next_vert}')
					q.enqueue(next_vert)
					# print(f'Enqueuing {next_vert}')

	def dft(self, starting_vertex):
		# print(f'Graph: {self.vertices}')
		stack = Stack()
		# print('starting vertex', starting_vertex)
		# print(f'Pushing starting vertex: {starting_vertex}')
		stack.push(starting_vertex)
		visited = set()
		while stack.size() > 0:
			vertex = stack.pop()
			if vertex not in visited:
				# print(f'We are at {vertex} and it not in {visited}')
				visited.add(vertex)
				# print(f'Added {vertex} to {visited}')
				for neighbor in self.vertices[vertex]:
					# print(f'Neighbors of {vertex}: {neighbor}')
					stack.push(neighbor)

	def dft_recursive(self, starting_vertex, visited=[]):
		if starting_vertex in visited:
			return visited
		else:
			print(f'{starting_vertex} not in {visited}')
			visited.append(starting_vertex)
			print(f'Appended {starting_vertex} to {visited}')
			for neighbor in self.vertices[starting_vertex]:
				print(f'Neighbors of {starting_vertex}: {neighbor}')
				self.dft_recursive(neighbor, visited)

	def bfs(self, starting_vertex, destination_vertex):
		"""
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
		pass  # TODO

	def dfs(self, starting_vertex, destination_vertex):
		"""
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
		pass  # TODO

	def dfs_recursive(self, starting_vertex, destination_vertex):
		"""
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
		pass  # TODO


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
