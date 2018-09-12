"""
Simple graph implementation compatible with BokehGraph class.
"""
import math

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.colors = {}
        self.x_positions = {}
        self.y_positions = {}

    def add_vertex(self, vertex, x = 0, y = 0, color = "#999"):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
            self.colors[vertex] = color
            self.x_positions[vertex] = x
            self.y_positions[vertex] = y
        else:
            raise Exception("This vertex has already been added")

    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
        else:
            raise Exception("One of your vertices doesn't exist")

    def bfs(self, start_vert):
        white_color = "#fff"
        gray_color = "#999"
        queue = []
        visited = []

        for v in self.vertices:
            self.colors[v] = white_color   

        self.colors[start_vert] = gray_color  
        queue.append(start_vert)
        while len(queue) > 0:
            u = queue[0]
            visited.append(u)
            for v in self.vertices[u]: 
                if v not in visited:
                    self.colors[v] = gray_color  
                    queue.append(v)
            queue.pop(0)

        return visited

    def dfs(self):
        stack = []

        for v in self.vertices:
            if v not in stack:
                self.dfs_util(v, stack)

    def dfs_util(self, v, visited):
        visited.append(v)
        
        for e in self.vertices[v]:
            if e not in visited:
                self.dfs_util(e, visited)