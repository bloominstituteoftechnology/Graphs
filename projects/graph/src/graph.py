#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        self.vertices.update({label: set()})

    def add_edge(self, start, end, bidirectional = True):
        if start not in self.vertices:
            raise Exception(f'{start} not a vertex')
        if end not in self.vertices:
            raise Exception(f'{end} not a vertex')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start=0, cb=lambda x: print(x), algo='breadth'):
        if algo == 'breadth':
            queue = list(list(self.vertices)[start])
            visited = set()

            while queue:
                current_vert = queue.pop(0)
                cb(current_vert)
                visited.add(current_vert)
                for child in self.vertices[current_vert]:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)
        
        elif algo == 'depth':
            stack = list(list(self.vertices)[start])
            visited = set()

            while stack:
                current_vert = stack.pop()
                cb(current_vert)
                visited.add(current_vert)
                for child in self.vertices[current_vert]:
                    if child not in visited:
                        stack.append(child)
                        visited.add(child)
