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
        self.vertices[vert].add(value)
        self.vertices[value].add(vert)


def bft(self, starting_node):
    # Create a Queue
    q = Queue()
    visited = set()
    # Enqueue the starting node
    q.enqueue(starting_node)
    # While the queue is not empty
    # Dequeue a node from the queue
    # Mark it as visited
    # Enqueue all of its children that have not been visted


def dft(self, starting_node):
    # Create a Stack
    s = Stack()
    visited = set()
    # Push the starting node
    s.push(starting_node)
    # While the stack is not empty
    # Pop a node from the stack
    # Mark it as visited
    # Push all of its children that have not been visted


def dft_r(self, starting_node, visted=None):
    if visited is None:
        visited = set()
    # If the node has not been visited
        # Mark the node as visted
        # Call dft_r on all children
        deft_r(child_node, visited)


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
