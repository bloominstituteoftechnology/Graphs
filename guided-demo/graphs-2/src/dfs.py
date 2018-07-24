#!/usr/bin/python

"""
Represent a graph with depth-first-search, and run a demo with a randomly
generated graph containing a given number of vertices and edges (default 8).
"""

from sys import argv


class Vertex:
    """Represent a vertex with label and set of edges to other vertices."""
    # Just holds data, but is class and not namedtuple/dict so it is hashable
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __str__(self):
        return "Vertex " + str(self.label)


class Graph:
    """Represent a graph and enable depth-first search."""
    def __init__(self):
        self.vertices = set()

    def add_edge(self, vertex_a, vertex_b):
        """Add a *bidirectional* edge between two vertices."""
        if vertex_a not in self.vertices or vertex_b not in self.vertices:
            raise Exception('Vertices to connect not in graph!')
        vertex_a.edges.add(vertex_b)
        vertex_b.edges.add(vertex_a)

    def dfs(self, start, target=None):
        """Perform depth-first search from a start, to optional target."""
        if start not in self.vertices:
            raise Exception('Start vertex not in graph!')

        visit_stack = [start]
        visited = set()
        while visit_stack:
            visiting = visit_stack.pop()
            visited.add(visiting)
            visiting.color = 'gray'
            if target and visiting == target:
                print('Found target:', visiting)
                return
            visit_stack.extend(visiting.edges - visited)

        if target:
            print('Target not found!')


def main(num_vertices=8, num_edges=8):
    """Build demo graph and execute DFS."""
    graph = Graph()
    for num in range(num_vertices):
        graph.vertices.add(Vertex(label=str(num)))

    # Add some random edges
    from random import sample
    for _ in range(num_edges):
        vertices = sample(graph.vertices, 2)
        graph.add_edge(vertices[0], vertices[1])

    # DFS with random start/target
    start, target = sample(graph.vertices, 2)
    graph.dfs(start, target)


if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = argv[1]
        NUM_EDGES = argv[2]
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()  # accept defaults
