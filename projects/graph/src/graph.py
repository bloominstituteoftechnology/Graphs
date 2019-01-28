"""
Simple graph implementation
"""

import queue as queue

class Vertex:
    def __init__(self, vertex_value):
        self.value = vertex_value
        self.edges = set()

    def __repr__(self):
        return f'{self.value}'


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        

    def add_vertex(self,key):
        self.vertices[key] = Vertex(key)

    def add_edge(self,ver1,ver2):
        if ver1 in self.vertices and ver2 in self.vertices:
            self.vertices[ver1].edges.add(ver2)
            self.vertices[ver2].edges.add(ver1)
            

    def bft(self, starting_node):
        if self.vertices == None:
            return

        if starting_node not in self.vertices:
            return None

        visited = []
        storage = queue.Queue()
        storage.put(self.vertices[starting_node])

        while not storage.empty():
            current = storage.get()

            if current not in visited:
                visited.append(current)

            for edge in current.edges:
                if self.vertices[edge] not in visited:
                    storage.put(self.vertices[edge])

        return visited

    def dfs(self, starting_node):
        stack = [self.vertices[starting_node]]
        visited = []

        while len(stack) > 0:
            current = stack.pop()
            visited.append(current)

            for edge in current.edges:
                if self.vertices[edge] not in visited:
                    stack.append(self.vertices[edge])

        return visited

    def dft_r(self, starting_node, visited = None):
        #mark the node as visited
        #call dft_r on all children
        visited.append(starting_node)

        for edge in self.vertices[starting_node].edges:
            if edge not in visited:
                self.dft_r(edge, visited)

        return visited