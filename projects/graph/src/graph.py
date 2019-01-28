"""
Simple graph implementation
"""
from collections import deque

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

    def bfs(self, starting_vertex):
        #Used to keep track of visited verticies
        visited = []
        # Create a queue
        queue = deque()

        queue.append(starting_vertex)
        # Mark first vertex as visited
        # Enqueue the starting node
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                neighbors = self.vertices[vertex]

                for neighbor in neighbors:
                    queue.append(neighbor)
        return visited
    
    def dfs_recursive(self, starting_vertex, visited = []):
        visited.append(starting_vertex)
        print(starting_vertex)

        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                self.dfs_recursive(vertex, visited)
