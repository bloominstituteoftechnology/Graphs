"""
Simple graph implementation compatible with BokehGraph class.
"""

# super really basic vec2 class
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # add
    def add(self, other):
        self.x += other.x
        self.y += other.y

    # subtract
    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y

    # multiply
    def multiply(self, other):
        self.x *= other.x
        self.y *= other.y

    # divide (integer)
    def divide(self, other):
        self.x //= other.x
        self.y //= other.y


# Queue for BFS
class Queue:
    def __init__(self):
        self.storage = []
    
    # enqueue method
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue method
    def dequeue(self):
        return self.storage.pop(0) if self.size() > 0 else None


    # size method
    def size(self):
        return len(self.storage)


# Stack for DFS (copied my queue class and removed the argument from pop)
class Stack:
    def __init__(self):
        self.storage = []
    
    # enqueue method
    def enqueue(self, value):
        self.storage.append(value)

    # dequeue method
    def dequeue(self):
        return self.storage.pop() if self.size() > 0 else None


    # size method
    def size(self):
        return len(self.storage)




# implement the basics of a vertex class
class Vertex:
    def __init__(self, id, pos, colour = None, data = None):
        self.id = int(id)
        self.pos = Vec2(0, 0) if pos is None else pos
        self.colour = "white" if colour is None else colour
        self.data = F"v{self.id}" if data is None else data
        self.edge = set() # refactored vertex to hold its connecting edges

    def __str__(self):
        return F"Vertex( id: {self.id}, x: {self.pos.x}, y: {self.pos.y}, data: {self.data})"




class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices = None):
        self.vertices = {} if vertices is None else vertices

    # add_vertex method
    def add_vertex(self, id, pos, data):
        self.vertices[id] = Vertex(id, pos, data = data)

    # TODO: serch method

    # add_edge method (bi directional as default to start with)
    def add_edge(self, vertex_a, vertex_b, bidir=True):
        if vertex_a not in self.vertices or vertex_b not in self.vertices:
            return "ERROR!!!! : out of index" # TODO: change this to an exception later
        self.vertices[vertex_a].edges.add(vertex_b)
        if bidir:
            self.vertices[vertex_b].edges.add(vertex_a)

# some basic tests for the vertex class

#constructor test
v0 = Vertex('0', Vec2(3, 4))

# raw positional data manipulation test
v0.pos.x = 23

# vector add test
v0.pos.add(Vec2(10, 10))

# vertex print test
print(v0)

g0 = Graph()
g0.add_vertex(v0.id, v0.pos, "Node0")

print(g0)