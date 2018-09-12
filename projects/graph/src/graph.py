class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex, new_edge):
        if vertex not in self.vertices:
            raise Exception("Vertex does not exist!")
        self.vertices[vertex].add(new_edge)
