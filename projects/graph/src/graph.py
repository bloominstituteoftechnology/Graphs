"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    # def __init__(self):
    #     self.vertices = {}

    # def add_vertex(self, v):
    #     if v is not None:
    #         self.vertices[v] = set()
    #     else:
    #         return "Error: Vertex can not be none"

    # def add_edge(self, vertex1, vertex2):
    #     if vertex1 and vertex2:
    #         self.vertices[vertex1].add(vertex2)

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
        else:
            undefined = []
            if vertex1 not in self.vertices:
                undefined.append(vertex1)
            if vertex2 not in self.vertices:
                undefined.append(vertex2)
            undefined = ", ".join(undefined)
            raise KeyError(f"Vertex not found: {undefined}")
