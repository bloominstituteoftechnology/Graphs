#!/usr/bin/python
"""Graph representation using adjacency list."""
class Vertex:
    """Vertices have a label and a set of edges and possible connected component."""
    def __init__(self, label, component=-1):
        self.label = label
        self.component = component
        self.edges = {}

    def __repr__(self):
        return self.label

"""
Simple graph implementation compatible with BokehGraph class.
"""

vertex = Vertex(label="", component=-1)

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

    def search(self, start, target=None, method="dfs"):
        if start not in self.vertices:
            raise Exception("Start vertex not in graph!")
        quack = [start] #queue or stack depending on method
        pop_index = 0 if method == "bfs" else -1
        visited = set()
        

        while quack:
            visiting = quack.pop(pop_index)
            if visiting == target:
                print("Target {} found".format(target))
            visited.add(visiting)
            quack.extend(self.vertices[visiting] - visited)
        print("visited", visited)
        return visited

    