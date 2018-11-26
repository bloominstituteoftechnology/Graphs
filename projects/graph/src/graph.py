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

# TODO: add some data structures for searching method

# TODO: Queue for BFS

# TODO: Stack for DFS


# implement the basics of a vertex class
class Vertex:
    def __init__(self, id, pos, colour = None, data = None):
        self.id = int(id)
        self.pos = Vec2(0, 0) if pos is None else pos
        self.colour = "white" if colour is None else colour
        self.data = F"v{self.id}" if data is None else data

    def __str__(self):
        return F"Vertex( id: {self.id}, x: {self.pos.x}, y: {self.pos.y}, data: {self.data})"




class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices = None):
        self.vertices = {} if vertices is None else vertices

        # TODO: add_vertex method

        # TODO: serch method
        pass  # TODO

# some basic tests for the vertex class

#constructor test
v0 = Vertex('0', Vec2(3, 4))

# raw positional data manipulation test
v0.pos.x = 23

# vector add test
v0.pos.add(Vec2(10, 10))

# vertex print test
print(v0)