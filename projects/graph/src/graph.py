"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
import math

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    # def add_vertex(self, v):
    #     self.vertices[v] = set()
    def add_vertex(self, v):
        self.vertices[v] = Vertex(v)
    def add_edge(self, v1, v2):
        self.vertices[v1].edges.add(v2)
        self.vertices[v2].edges.add(v1)
    def dfs(self, value, visited=None):
        if visited is None: 
            visited = []
        visited.append(value)
        for vert in self.vertices:
            print(vert)
            if value == vert:
                return True 
            else:
                print(self.vertices[vert].edges, '26')
                verts = self.vertices[vert]
                print(verts, '28')
                for edge in verts.edges:
                    self.dfs(edge, visited)
        return False 
    def bfs(self, value): 
        # do BfS 
        searched = []
        queue = [self.vertices[0]]
        return False

class Vertex: 
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x is None: 
            self.x = math.floor(random.random() * 10 )+1
        else: 
            self.x = x
        if y is None: 
            self.y = math.floor(random.random() * 10)+1
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

