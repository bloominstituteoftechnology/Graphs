"""Graph representation using adjacency matrix."""

class Vertex:
    """Vertices just need a label, the matrix will track edges."""
    # Using simple classes for illustrative purposes
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label


class Graph:
    """The graph is a matrix of 0s/1s indicating existence of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, num_vertices):
        # * copying is shallow, so need explicit iteration for unique rows
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def connect_vertex(self, row, col):
        """Add an edge between vertices indicated by row/col of matrix."""
        self.matrix[row][col] = 1
