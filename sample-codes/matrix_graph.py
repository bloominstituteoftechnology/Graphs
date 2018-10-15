"""Live coding of different ways to represent graphs."""

class Vertex:
    """MVV - Minimum Viable Vertex."""
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return str(self.label)

class MatrixGraph:
    """Adjacency matrix representation of a graph."""
    def __init__(self, num_vertices):
        self.matrix = [[0 for _ in range(num_vertices)]
                        for _ in range(num_vertices)]
        self.vertices = [Vertex(str(i)) for i in range(num_vertices)]

    def add_edge(self, start_index, end_index, bidirectional=True):
        """Add an edge from start vertex to end vertex."""
        self.matrix[start_index][end_index] = 1
        if bidirectional:
            self.matrix[end_index][start_index] = 1