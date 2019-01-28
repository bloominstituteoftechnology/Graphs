from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self, item):
        return self.stack.pop()


"""
Simple graph implementation
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, id):
        if id not in self.vertices:
            self.vertices[id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("No vertex")

    def bft(self, starting_vertex):
        visited = []

        queue = deque()
        queue.append(starting_vertex)
        
        while len(queue) > 0:
            current = queue.popleft()
            print(current)
            visited.append(current)

            for item in self.vertices[current]:
                if item not in visited:
                    queue.append(item)