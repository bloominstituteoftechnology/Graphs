#!/usr/bin/python
from draw import BokehGraph


"""
Simple graph implementation compatible with BokehGraph class.
"""

# """
# Simple graph implementation compatible with BokehGraph class.
# """


class Vertex:
    """Vertices have a label and a set of edges."""

    def __init__(self, label, x, y, color="gray"):
        self.label = label
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.color = color
        self.edges = set()

    def __repr__(self):
        if self.pos:
            return "{}, ({}, {}), {}, {}".format(
                self.label, self.x, self.y, self.color, self.edges
            )


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return str(self.vertices)

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if isinstance(start, Vertex):
            start = start.label
        if isinstance(end, Vertex):
            end = end.label

        if start not in list(self.vertices.keys()):
            self.add_vertex(Vertex(start))
        if end not in list(self.vertices.keys()):
            self.add_vertex(Vertex(end))

        self.vertices[start].edges.add(self.vertices[end])
        if bidirectional:
            self.vertices[end].edges.add(self.vertices[start])

    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)
        if vertex.label in self.vertices:
            raise Exception("Error: Vertex already exists.")
        self.vertices[vertex.label] = vertex


def main():
    v0 = Vertex("0", 20, 7, "gray")
    v1 = Vertex("1", 40, 20, "black")
    v2 = Vertex("2", 15, 2, "gray")
    v3 = Vertex("3", 5, 15, "gray")
    graph = Graph()
    graph.add_vertex(v0)
    graph.add_vertex(v1)
    graph.add_vertex(v2)
    graph.add_vertex(v3)
    graph.add_edge(v1, v2)
    graph.add_edge(v2, v3, False)

    b = BokehGraph(graph)
    b.show()


if __name__ == "__main__":
    main()
