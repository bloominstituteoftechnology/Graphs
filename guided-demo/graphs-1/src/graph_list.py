class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []


class Graph:
    def __init__(self):
        self.vertices = []
