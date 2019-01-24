"""
Simple graph implementation
"""


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        return self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)


class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.edges = set()

    def __repr__(self):
        return f"Edges: {self.edges}, V: {self.vertex}"


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self, name):
        self.vertices = {}
        self.name = name

    def __repr__(self):
        return f"{self.name}: {self.vertices}"

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.vertices[value] = vertex

    def add_edge(self, vertex_name, edge):
        self.vertices[vertex_name].edges.add(edge)

    def get_vert(self, name):
        return {name: self.vertices.get(name)}

    def bft(self, starting_node):
        q = Queue()
        visited = set()
        q.enqueue(starting_node)
        while q.size() > 0:
            node = q.dequeue()
            if node not in visited:
                visited.add(node)
                print(node)
                for child in self.vertices[node].edges:
                    q.enqueue(child)

    def dft(self, starting_node):
        s = Stack()
        visited = set()
        s.push(starting_node)
        while s.size() > 0:
            node = s.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                for child in self.vertices[node].edges:
                    s.push(child)


g = Graph("Graph")
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 3)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(6, 2)
g.add_edge(7, 1)
g.dft(3)

print(g)
