from queue import Queue

"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):

        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
        else:
            raise Exception("Edges to nonexistent vetices")

    def bredth_first_traversal(self, start_node):
        queue = Queue()
        visited = set()
        queue.enqueue(start_node)
        while queue:
            visited.add(queue.dequeue())
