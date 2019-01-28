from collections import deque

"""
Simple graph implementation
"""


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        self.vertices[vertex].add(edge)

    # Breadth First Traversal

    def bft(self, starting_node):
        # Create a queue
        queue = deque()
        # create a visited list
        visited = set()
        # mark the first node as visited
        # enqueue the starting node
        queue.append(starting_node)
        # while queue is not empty
        while queue:
            pass
            # -> dequeue a node from queue
            # -> mark it as visited
            # -> enqueue all of it's children

    # Depth First Traversal

    def dft(self, starting_node):
        # Create a stack
        stack = deque()
        # create a visited list
        visited = set()
        # mark the first node as visited
        # enstack the starting node
        stack.append(starting_node)
        # while stack is not empty
        while stack:
            pass
            # -> destack a node from stack
            # -> mark it as visited
            # -> enstack all of it's children

    def dft_rec(self, starting_node, visted=None):
        # create visited
        if visited is None:
            visted = set()
        # If the node has not been visited
        # Mark the node as visited
        # call dft_rec on all children

    # Breadth First Search

    def bfs(self, starting_node, target_node):
        # Create a queue
        queue = deque()
        # create a visited list
        visited = set()
        # mark the first node as visited
        # enqueue the starting node
        queue.append(starting_node)
        # while queue is not empty
        while queue:
            pass
            # -> dequeue a node from queue
            # -> mark it as visited
            # -> if node == target return True
            # -> enqueue all of it's children


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
