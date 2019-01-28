from collections import deque

"""
Simple graph implementation
"""


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    Adjacency List!
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        self.vertices[vertex].add(edge)

    # Breadth First Traversal

    def bft(self, starting_vert):
        # Create a queue
        queue = deque()
        # create a visited list
        visited = set()
        # enqueue the starting vert
        queue.append(starting_vert)
        # while queue is not empty
        while queue:
            # -> dequeue a vert from queue
            dequeued = queue.popleft()
            # -> mark it as visited
            visited.add(dequeued)
            # -> enqueue all of it's children
            for vert in self.vertices[dequeued]:
                if vert not in visited:
                    queue.append(vert)
        return visited

    # Depth First Traversal

    def dft(self, starting_vert):
        # Create a stack
        stack = deque()
        # create a visited list
        visited = set()
        # enqueue the starting vert
        stack.append(starting_vert)
        # while stack is not empty
        while stack:
            # -> dequeue a vert from stack
            dequeued = stack.pop()
            # -> mark it as visited
            visited.add(dequeued)
            # -> enqueue all of it's children
            for vert in self.vertices[dequeued]:
                if vert not in visited:
                    stack.append(vert)
        return visited

    def dft_rec(self, starting_node, visted=None):
        # create visited
        if visited is None:
            visted = set()
        # If the node has not been visited
        # if
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
