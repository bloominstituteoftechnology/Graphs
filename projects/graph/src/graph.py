"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices):
        self.vertices = vertices
        def print_vertices(self,vertices):
            print(self.vertices)


print(Graph({'0': {'1', '3'},'1': {'0'},'2': set(),'3': {'0'}}).vertices)

