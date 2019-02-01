"""
Simple graph implementation
"""


class Stack:
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


class Queue:
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


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, parent, child):
        if parent in self.vertices and child in self.vertices:
            self.vertices[parent].add(child)
        else:
            print("One or more vertices, not in graph")

    def bft(self, vertex):
        q = Queue()
        visited = set()
        q.enqueue(vertex)
        while q.queue:
            node = q.dequeue()
            if node not in visited:
                print(node)
                visited.add(node)
                for vertex in self.vertices[node]:
                    q.enqueue(vertex)

    def dft(self, vertex):
        s = Stack()
        visited = set()
        s.push(vertex)
        while s.stack:
            node = s.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                for vertex in self.vertices[node]:
                    s.push(vertex)

    def dft_r(self, vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex)
        for vertex in self.vertices[vertex]:
            if vertex in visited:
                continue
            self.dft_r(vertex, visited)
