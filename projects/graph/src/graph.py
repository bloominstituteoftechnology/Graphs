#!/usr/bin/python
"""Graph representation using adjacency list."""
class Vertex:
    """Vertices have a label and a set of edges."""
    def __init__(self, label):
        self.label = label
        self.edges = {}

    def __repr__(self):
        return str(self.label)

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:    
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            raise Exception("Error: vertex already exists!")
        self.vertices[vertex] = set()
    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("supplied vertex not in graph!!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def BFS(self, s):
        visited = [False] * len(self.vertices)
        queue = []
        queue.append(s)
        visited[s] = True
        

        while len(queue) > 0:
            s = queue.pop(0)
            for i in self.vertices[s]:
                if  visited[i] == False:
                    queue.append(i)
                    visited[i] == True
                    print(queue)
                queue.remove(i)

    def DFS(self, s):
        stack = []
        visited = [False] * len(self.vertices)
        stack.append(s)
        visited[s] = True

        while len(stack)> 0:
            s= stack.pop()
            for i in self.vertices[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] == True
                    print(stack)
                stack.remove(i)