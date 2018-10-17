"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    def __init__(self):
        self.vertices = {}
        self.id = -1
    def createID(self):
        self.id += 1
        return self.id
    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name, self.createID())
        else:
            print("that vertex already exists")


class Vertex:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.edges = []
    def __repr__(self):
        return f"ID: {self.id}, Edges: {self.edges}, Name: {self.name}"
    def add_edge(self, destination):
        if destination not in self.edges:
            self.edges.append(destination)
        else:
            print("that edge already exists")


