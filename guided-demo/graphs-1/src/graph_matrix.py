"""Graph representation using adjacency matrix."""
import math

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
    
    def add_vertex(self, vertex):
        vertices_to_add = len(self.matrix) - (len(self.matrix) + 1)
        # new_row_integer = len(self.matrix)+1
        for i in new_row:
            i.append(0 * len(self.matrix)+1 )
        print(new_row)
    

        matrix_clone = self.matrix[:]
        for i in matrix_clone:
            i.append(0)
            # matrix_clone[.append([0])
            # matrix_clone.append(row_to_add)


graph = Graph(5)
print(graph.matrix)
graph.add_vertex(6)
print(graph.matrix)