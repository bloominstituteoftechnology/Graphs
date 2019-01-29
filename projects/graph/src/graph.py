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
        # Create a new queue using the imported queue file
        queue = Queue()
        # Storage for the nodes that were visted
        visited = []
        # Enqueues the starting node
        queue.enqueue(start_node)
        # Checks if the queue size is greater than 0
        while len(queue.storage) > 0:
            visited.append(queue.dequeue())
            for c_node in self.vertices[queue.dequeue()]:
                if c_node not in visited:
                    queue.enqueue(c_node)
        return visited
