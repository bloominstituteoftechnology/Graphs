from collections import deque

"""
Simple graph implementation
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)
            self.vertices[vertex_2].add(vertex_1)
        else:
            if vertex_1 not in self.vertices and vertex_2 not in self.vertices:
                raise KeyError(f"{vertex_1} and {vertex_2} are not valid vertices")
            else:
                invalid_vertex = vertex_1 if vertex_1 not in self.vertices else vertex_2
                raise KeyError(f"{invalid_vertex} is not a valid vertex")

    def bft(self, start, q=deque(), visited=set()):
        if start in self.vertices:
            print(start)
            if len(visited) == 0:
                visited.add(start)
            for related in self.vertices[start]:
                if related not in visited:
                    q.append(related)
                    visited.add(related)
            if len(q) > 0:
                self.bft(q.popleft(), q, visited)

    def dft(self, start):
        pass

    def bfs(self, target):
        pass

    def dfs(self, target):
        pass
