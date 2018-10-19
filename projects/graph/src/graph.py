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

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self,vertex):#Vertices are keys in dictionary
        self.vertices[vertex] = set()
    def add_edge(self,start,end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
        else:
            raise IndexError("That vertex does not exist!")
    def dft(self, starting_node):
        s = Stack()
        s.push(starting_node)
        visited = []
        while s.size() > 0:

    def bft(self, starting_node):
        q = Queue()
        q.enqueue(starting_node)
        visited = []
        while q.size() > 0:
            

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)