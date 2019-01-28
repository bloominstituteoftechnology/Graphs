from collections import deque
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
        # Create a queue
        queue = deque()
        queue.extend(self.vertices[starting_vertex])
        # Mark first vertex as visited
        # Enqueue the starting node
        while len(queue) > 0:
            current = queue.popleft()
            print(current)
            if current not in visited:
                visited.append(current)
        return visited