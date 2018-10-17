"""
Simple graph implementation compatible with BokehGraph class.
"""
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, a):
        if (a not in self.vertices):
            self.vertices[a] = set()
        else:
            return print("Already a vertex")


    def add_edge(self, a, b):
        print(a)
        if(b not in self.vertices):
            print(f"Node {b} is not in vertex")
        else:
            self.vertices[a].add(b)

    def get_vertices(self):
        print(self.vertices)
        return self.vertices

    def bft(self, starting_node):
        q = Queue()
        q.enqueue(starting_node)
        visited = []
        while q.size() > 0:
            v = q.dequeue()
            if (v not in visited):
                visited.append(v)


    # Remove the first node from the queue...
    # If it has not been visited yet,...
    # Mark it as visited....
    # Then put all it's children in the back of the queue



