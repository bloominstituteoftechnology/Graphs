# Simple graph implementation


class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges.
    def __init__(self):
        # TODO
        # Create an empty graph
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, edge, vertex):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)
        else:
            print(f"No {vertex} vertex")

