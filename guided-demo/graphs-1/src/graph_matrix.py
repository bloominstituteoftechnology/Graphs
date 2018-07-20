class Vertex:
    def __init__(self, value):
        self.value = value


class Graph:
    def __init__(self, rows, cols):
        self.matrix = [[0] * cols] * rows

    def connect_vertex(self, a, b):
        self.matrix[a][b] = 1
