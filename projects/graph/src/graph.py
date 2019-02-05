"""
Simple graph implementation
"""
from collections import deque

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        if v1 and v2 in self.vertices:
            self.vertices[v1].update(v2)
            self.vertices[v2].update(v1)
        if v1 not in self.vertices:
            raise Exception(f"{v1} is not in self.vertices")
        if v2 not in self.vertices:
            raise Exception(f"{v2} is not in self.vertices")

    def BFT(self, start):
        d = deque()
        visited = []
        d.append(start)
        while d:
            vertex = d.popleft()
            if vertex not in visited:
                visited.append(vertex)
                next_nodes = self.vertices[vertex]
                for node in next_nodes:
                    d.append(node)
        return visited

    def DFT(self, start):
        s = []
        visited = []
        s.append(start)
        while len(s) > 0:
            vertex = s.pop()
            if vertex not in visited:
                visited.append(vertex)
                for child in self.vertices[vertex]:
                    s.append(child)
        return visited

    def DFTR(self, start, visited=None):
        if visited is None:
            visited = []
        if start not in visited:
            visited.append(start)
            for child in self.vertices[start]:
                self.DFTR(child, visited)
        return visited

    def BFS(self, start, end):
        d = deque()
        visited = []
        d.append(start)
        if end in self.vertices[start]:
            visited.append(start)
            visited.append(end)
            return visited
        while d:
            vertex = d.popleft()
            if vertex == end:
                visited.append(vertex)
                return visited
            if  end in visited:
                return visited
            if vertex not in visited:
                visited.append(vertex)
                next_nodes = self.vertices[vertex]
                for node in next_nodes:
                    d.append(node)
        return False
