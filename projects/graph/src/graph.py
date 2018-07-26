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
        queue = []
        order = []
        visited = set()
        queue.append(self)        

        while len(queue) > 0:
            current_vert = queue.pop(0)
            order.append(current_vert)
            visited.add(current_vert)
            for i in self.vertices[current_vert]:
                if i not in visited:
                    queue.append(i)
                    order.append(i)
        print(order)
        return order

    def DFS(self, s):
        stack = []
        order = []
        visited = set()
        stack.append(self)

        while len(stack)> 0:
            current_vert= stack.pop()
            visited.add(current_vert)
            order.append(current_vert)
            for i in self.vertices[current_vert]:
                if i not in visited:
                    stack.append(i)
                    order.append(i)
                    visited.add(i)
                stack.remove(i)
        print(order)
        return order