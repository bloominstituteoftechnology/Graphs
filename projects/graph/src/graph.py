"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

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
    def add_vertex(self, vert_id):
        self.vertices[vert_id] = Vertex(vert_id)
    def add_edge(self, vert1, vert2):
        if vert1 in self.vertices and vert2 in self.vertices:
            self.vertices[vert1].edges.add(vert2)
            self.vertices[vert2].edges.add(vert1)
        else:
            raise IndexError('Vertex does not exist')
    def add_directed_edge(self, vert1, vert2):
        if vert1 in self.vertices:
            self.vertices[vert1].edges.add(vert2)
        else:
            raise IndexError('Vertex does not exist')
    def dft_st(self, starting_node):
        s = Stack()
        s.push(starting_node)
        visited = []
        while s.size() > 0:
            current = s.pop()
            if current not in visited:
                visited.append(current)
                print(visited)
                for edge in self.vertices[current].edges:
                    s.push(edge)

    def bft(self, starting_node):
        q = Queue()
        q.enqueue(starting_node)
        visited = []
        while q.size() > 0:
            current = q.dequeue()
            if current not in visited:
                visited.append(current)
                print(visited)
                for edge in self.vertices[current].edges:
                    q.enqueue(edge)

            

class Vertex:
    def __init__(self, vert_id, x=None, y=None):
        self.id = vert_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    def __repr__(self):
        return "{}".format(self.edges)
    #     return f"{self.edges}"


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)