"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vert, value):
        if value in self.vertices:
            self.vertices[vert].add(value)
            self.vertices[value].add(vert)
        else:
            print(f'{value} is not a vertex')

    def bft(self, starting_node):
        # Create a Queue
        q = Queue()
        visited = []
        # Enqueue the starting node
        q.enqueue(starting_node)
        # While the queue is not empty
        while len(q.storage) > 0:
            # Dequeue a node from the queue
            node = q.dequeue()
            # Mark it as visited
            visited.append(node)
            # Enqueue all of its children that have not been visted
            for child in self.vertices[node]:
                if child not in visited:
                    q.enqueue(child)

        return visited

    def dft(self, starting_node):
        # Create a Stack
        s = Stack()
        visited = []
        # Push the starting node
        s.push(starting_node)
        # While the stack is not empty
        while len(s.storage) > 0:
            # Pop a node from the stack
            node = s.pop()
            # Mark it as visited
            visited.append(node)
            # Push all of its children that have not been visted
            for child in self.vertices[node]:
                if child not in visited:
                    s.push(child)

        return visited

    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited = []
        # If the node has not been visited
        if starting_node not in visited:
            visited.append(starting_node)
            # Mark the node as visted
            # Call dft_r on all children
            for child in self.vertices[starting_node]:
                if child not in visited:
                    self.dft_r(child, visited)
        return visited


def bfs(self, starting_node, target_node):
    # Create a Queue
    q = Queue()
    visited = set()
    # Enqueue the starting node
    q.enqueue(starting_node)
    # While the queue is not empty
    # Dequeue a node from the queue
    # Mark it as visited
    # If node == target_node: return True
    # Enqueue all of its children that have not been visted
    # return False


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.pop(0)


class Stack:
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()
