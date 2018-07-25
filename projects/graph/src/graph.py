#!/usr/bin/python
import pprint

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)


# Adjacency list type
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges"""

    def __init__(self):
        # I think the bokeh wants the vertices as a dict
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices"""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent verticies')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """Add a edge (default bidirectional) between two vertices"""
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error: Vertices not in graph")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_edge("0", "1")
    graph.add_edge("0", "3")
    print(graph.vertices)


if __name__ == "__main__":
    main()
