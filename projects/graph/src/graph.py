#!/usr/bin/python
from draw import BokehGraph
from sys import argv
import random


"""
Simple graph implementation compatible with BokehGraph class.
"""

# """
# Simple graph implementation compatible with BokehGraph class.
# """


class Vertex:
    """Vertices have a label and a set of edges."""

    def __init__(self, label, color="gray", **pos):
        self.label = label
        self.color = color
        self.pos = pos
        self.edges = set()

    def __repr__(self):
        return "{}, {}, {}".format(self.label, self.color, self.edges)

    def __str__(self):
        if not self.pos:
            pos = dict(x=None, y=None)
        if self.pos:
            return "Vertex is {}, at position ({}, {}), color is {}, and has edges {}".format(
                self.label, pos["x"], pos["y"], self.color, self.edges
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

    def bfs(self, start=None):
        if not start:
            print(list(self.vertices.items()))
        random_color = "#" + "".join(
            [random.choice("0123456789ABCDEF") for j in range(6)]
        )
        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color
        for v in self.vertices.items():
            print("self.vertices.items():", self.vertices.items(), "\nv:", v)
        #     if v not in visited:
        #         queue.append(v)
        #         found.append()
        #     while len(queue) > 0:
        #         v = queue[0]
        #         for edge in v.edges:
        #             if edge not in found:
        #                 found.append(edge)
        #                 queue.append(edge)
        #                 edge.color = random_color

        #     queue.pop(0)
        # return found

    def connected_components(self):
        searched = []

        for index, vertex in self.vertices.items():
            if vertex not in searched:
                searched.append(self.bfs(vertex))
        return searched


def main(num_vertices=8, num_edges=8):
    graph = Graph()
    if num_vertices:
        # Add appropriate number of vertices
        for num in range(num_vertices):
            graph.add_vertex(Vertex(str(num)))
        #  Add random edges between vertices
        for _ in range(num_edges):
            vertices = random.sample(graph.vertices.keys(), 2)
            graph.add_edge(vertices[0], vertices[1])
    else:
        v0 = Vertex("0")
        v1 = Vertex("1")
        v2 = Vertex("2")
        v3 = Vertex("3")
        graph.add_vertex(v0)
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)
        graph.add_edge(v1, v2)
        graph.add_edge(v2, v3, False)
        graph.bfs()

    b = BokehGraph(graph)
    b.show()


if __name__ == "__main__":
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()
