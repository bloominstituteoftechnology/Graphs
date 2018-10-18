"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Queue:
  def __init__(self):
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)

  def dequeue(self):
    if len(self.storage) > 0:
        return self.storage.pop(0)
    else:
        return None

  def size(self):
    return len(self.storage)

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
        print("size={}".format(q.size()))
        while q.size() > 0:
            current = q.dequeue()
            print("size={}".format(q.size()))

            # print(current.id)
            visited.append(current.id)
            for edge in current.edges:
                if edge not in visited:
                    q.enqueue(self.vertices[edge])
        print(visited)

    def dft(self, starting_v):
        stack = []
        visited = []
        stack.append(self.vertices[starting_v])
        while len(stack) > 0:
            vstd_node = stack.pop()
            if vstd_node.id not in visited:
                visited.append(vstd_node.id)
                for edge in vstd_node.edges:
                    stack.append(self.vertices[edge])
        print(visited)




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
