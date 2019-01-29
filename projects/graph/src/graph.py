from queue import Queue

"""
Simple graph implementation
"""


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


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
        else:
            raise Exception(f'Vertex {vertex1} does not exist.')

    def bredth_first_traversal(self, start_node):
        # Create a new queue using the imported queue file
        queue = Queue()
        # Storage for the nodes that were visted
        visited = []
        # Enqueues the starting node
        queue.enqueue(start_node)
        # Checks if the queue size is greater than 0
        while queue.len() > 0:
            node = str(queue.dequeue())
            visited.append(node)
            for c_node in self.vertices[node]:
                if c_node not in visited:
                    queue.enqueue(c_node)
        return visited

    # def depth_first_traversal(self, start_node):
    #     stack = []
    #     visited = []
    # def depth_first_traversal_recursive(self, start_node):
    #     if visited is None:
    #         visited = set()
    #     visited.add(start_node)
    #     print(Starting_node)
    #     for child_node in self.vertices[start_node]
    #     if child_node not in visited:
    #             self.depth_first_traversal_recursive(child_node, visited)
    #             depth_first_Traversal_recursive(child_node, visited)
