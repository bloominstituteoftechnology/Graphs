class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = set()


class Graph:
    def __init__(self):
        self.vertices = set()
