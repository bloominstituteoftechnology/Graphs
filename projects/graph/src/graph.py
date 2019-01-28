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
        # Print
        print("BFT NODES VISITED:")
        # while queue is not empty
        while queue:
            # -> dequeue a vert from queue
            dequeued = queue.popleft()
            # -> mark it as visited
            if dequeued not in visited:
                visited.add(dequeued)
                print(dequeued)
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
        # Print
        print("DFT NODES VISITED:")
        # while stack is not empty
        while stack:
            # -> dequeue a vert from stack
            dequeued = stack.pop()
            # -> mark it as visited
            if dequeued not in visited:
                visited.add(dequeued)
                print(dequeued)
            # -> enqueue all of it's children
            for vert in self.vertices[dequeued]:
                if vert not in visited:
                    stack.append(vert)
        return visited

    def dft_rec(self, starting_vert, visited=None):
        # create visited
        if visited is None:
            visited = set()
        # Mark the node as visited
        if starting_vert not in visited:
            visited.add(starting_vert)
            print(starting_vert)
        # If the node has not been visited
        for vert in self.vertices[starting_vert]:
            if vert not in visited:
                self.dft_rec(vert, visited)

    # Breadth First Search

    def bfs(self, starting_vert, target_vert):
        queue = deque()
        visited = set()
        queue.append(starting_vert)
        # while queue is not empty
        while queue:
            # -> dequeue a vert from queue
            dequeued = queue.popleft()
            # check if target vert
            if dequeued == target_vert:
                return True
            # -> mark it as visited
            if dequeued not in visited:
                visited.add(dequeued)
            # -> enqueue all of it's children
            for vert in self.vertices[dequeued]:
                if vert not in visited:
                    queue.append(vert)

        return False
