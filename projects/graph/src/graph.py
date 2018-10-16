"""
Simple graph implementation compatible with BokehGraph class.
"""

import random
import json

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].edges.add(vertex2)
            self.vertices[vertex2].edges.add(vertex1)
        else:
            raise IndexError("That vertex does not exist")

    def dfs(self, starting_node, visited=None):
        if visited is None:
            visited = [False] * len(self.vertices)
        stack = [starting_node]
        results = []
        visited[starting_node] = True
        while stack:
            current_node = stack.pop()
            results.append(current_node)
            for next_node in self.vertices[current_node]:
                if visited[next_node] == False:
                    stack.append(next_node)
                    visited[next_node] = True
        return results

    # def add_directed_edge(self, vertex1, vertex2):
    #     if vertex1 in self.vertices:
    #         self.vertices[vertex1].edges.add(vertex2)
    #     else:
    #         raise IndexError("That vertex does not exist")
            
    # def add_vertex(self, vertex):
    #     self.vertices[vertex] = set()

    # def add_edge(self, vertex1, vertex2):
    #     if vertex1 in self.vertices and vertex2 in self.vertices:
    #         self.vertices[vertex1].add(vertex2)
    #         self.vertices[vertex2].add(vertex1)
    #     else:
    #         print('Invalid vertex(ices)')

class Vertex:
    def __init__(self, vertex_id, x = None, y = None):
        self.id = vertex_id
        self.edges = set()
        if x == None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y == None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    
    def __repr__(self):
        return f"{self.edges}"
        # return json.dumps(self.edges)