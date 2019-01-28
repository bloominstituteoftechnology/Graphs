"""
Simple graph implementation
"""
class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else: return None

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else: return None

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            return

    def add_edge(self, vertex_one, vertex_two):
        if vertex_one in self.vertices and vertex_two in self.vertices:
            self.vertices[vertex_one].add(vertex_two)
            self.vertices[vertex_two].add(vertex_one)
