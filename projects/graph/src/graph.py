from queue import Queue
"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex:
            self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)

    def bft(self, starting_node):
        q = Queue()
        visited = set()
        visited.add(starting_node)
        q.Enqueue(starting_node)
        while q.len() > 0:
            node = q.dequeue()
            if node not in visited:
                visited.append(node)
                for i in self.vertices[node]:
                    q.enqueue(i)

    def dft(self, starting_node):
        stack = [starting_node]
        visited = set()
        while len(stack) > 0:
            node = stack.pop()
            if node not in visited:
                for i in self.vertices[node]:
                    stack.append(i)

    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_node)
        for i in self.vertices[starting_node]:
            if i not in visited:
                self.dft_r(i, visited)
