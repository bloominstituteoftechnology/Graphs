"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vertex, value):
        # Add edge as a value to the vertex
        self.vertices[vertex].add(value)
        # Add vertex as a value to the edge
        self.vertices[value].add(vertex)
    
    def bfs(self, starting_node):
        # create a queue
        q = Queue()
        visited = set()
        # Enqueue the starting node
        q.Enqueue(starting_node)
       # While the queue is not empty
        while len(q.storage) > 0:
            # Dequeue a node from the queue
            node = q.dequeue()
            # Mark it as visited
            visited.append(node)
            # Enqueue all of its children that have not been visted
            for child in self.vertices[node]:
                if child not in visited:
                    q.enqueue(child)

        return visited
class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.pop(0)