"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vertex, value):
        # Add edge as a value to the vertex
        self.vertices[vertex].add(value)
        # Add vertex as a value to the edge
        self.vertices[value].add(vertex)
    
    def bfs(self, starting_node):
        # create a queue
        q = Queue()
        visited = set()
        # Enqueue the starting node
        q.Enqueue(starting_node)
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

    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited = []
        # If the node has not been visited
        if starting_node not in visited:
            visited.append(starting_node)
            # Mark the node as visited
            # Recursion through children
            for child in self.vertices[starting_node]:
                if child not in visited:
                    self.dft_r(child, visited)
        return visited

class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.pop(0)

class Stack:
    def __init__(self):
        pass  # TODO
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()