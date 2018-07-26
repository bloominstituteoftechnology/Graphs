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

    def BFS(self, start, target=None):
        if start not in self.vertices:
            raise Exception("Start vertex not in graph!")
        visit_queue = [start]
        order = []
        visited = set()
        

        while visit_queue:
            visiting = visit_queue.pop(0)
            visited.add(visiting)
            order.append(visiting)
            for i in self.vertices[visiting]:
                if i not in visited and i not in visit_queue:
                    visit_queue.append(i)
                    print(visit_queue)
        print("BFS visited", order)

    def DFS(self, start, target=None):
        if start not in self.vertices:
            raise Exception("Start vertex not in graph!")
        visit_stack = [start]
        visit_order = []
        visited = set()
        

        while visit_stack: ##not sure why this is producing trips to nodes multiple times.
            visiting= visit_stack.pop(-1)
            visited.add(visiting)
            visit_order.append(visiting)
            for i in self.vertices[visiting]:
                if i not in visited and i not in visit_stack:
                    visit_stack.append(i)
                    visit_order.append(i)
        print("DFS visit", visit_order)
        return visit_order   
