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
        queue = deque()
        queue.append(starting_vertex)
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                print(visited[-1:][0])
                next_layer = self.vertices[vertex]
                for node in next_layer:
                    if node not in queue and node not in visited:
                        queue.append(node)
        return visited


    def dft(self, starting_vertex):
        visited = []
        # Create a stack
        stack = [starting_vertex]
        # Mark first vertex as visited
        # push the starting node
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                print(visited[-1:][0])
                next_layer = self.vertices[current]
                for node in next_layer:
                    if node not in stack and node not in visited:
                        stack.append(node)
        return visited

    def dft_recursive(self, starting_vertex, visited=[]):
        visited = visited + [starting_vertex]
        print(visited[-1:][0])
        for next_level in self.vertices[starting_vertex]:
            if next_level not in visited:
                visited =  self.dft_recursive(next_level, visited)
        return visited
