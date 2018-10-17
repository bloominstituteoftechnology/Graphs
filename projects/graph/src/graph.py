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
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if not vertex_id in self.vertices:
            self.vertices[vertex_id] = Vertex(vertex_id)
        else:
            raise Exception('That vertex already exits!')

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if not v1 in self.vertices[v2].edges:
                self.vertices[v1].edges.add(v2)
                self.vertices[v2].edges.add(v1)
            else:
                raise Exception('That edge already exits!')
        else:
            raise IndexError("That vertex does not exist!")

    def dft(self):
        cc_list = []
        visited = []
        for node in self.vertices:
            if node not in visited:
                connected_components = []
                stack = Stack()
                stack.push(node)
                while stack.size() > 0:
                    current = stack.pop()
                    if current not in visited:
                        visited.append(current)
                        connected_components.append(current)
                        for edge in self.vertices[current].edges:
                            stack.push(edge)
                cc_list.append(connected_components)
        return cc_list

    def bft(self, starting_node):
        visited = []
        q = Queue()
        q.enqueue(starting_node)
        while q.size() > 0:
            current = q.dequeue()
            if current not in visited:
                visited.append(current)
                for edge in current.edges:
                    q.enqueue(self.vertices[edge])


class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 20 - 10
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 20 - 10
        else:
            self.y = y
            
    def __repr__(self):
        return f"{self.edges}, x = {round(self.x, 2)}, y = {round(self.y, 2)}"