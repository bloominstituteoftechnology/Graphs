"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, item):
    self.size = self.size + 1
    self.storage.append(item)

  def dequeue(self):
    if self.size > 0:
        self.size = self.size - 1
        return self.storage.pop(0)
    else:
        return None

  def len(self):
    return self.size

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vert_id):
        self.vertices[vert_id] = Vertex(vert_id)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("One or both of these vertices does not exist!")
    def bft(self, starting_v):
        q = Queue()
        visited = []
        q.enqueue(self.vertices[starting_v])
        while len(q.storage) != 0:
            edges = q[0].edges
            for edge in edges:
                q.enqueue(self.vertices[edge])
            if q[0].id not in visited:
                visited.append(q.dequeue())
            else:
                q.dequeue()
        visited = [i.id for i in visited]
        return visited

    def dft(self, starting_v):
        stack = []
        visited = []
        stack.append(self.vertices[starting_v])
        while len(stack) != 0:
            edges = stack[0].edges
            vstd_node = stack.pop()
            if q[0] not in visited:
                visited.append(vstd_node)
            for edge in edges:
                stack.append(self.vertices[edge])
            



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
