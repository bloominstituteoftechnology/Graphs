"""
Simple graph implementation
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        pass  # TODO

    def add_vertex(self, vertex):
        new_vertex = { vertex : set() }
        self.vertices.update(new_vertex)

    def add_edge(self, edge_one, edge_two):
        for key in self.vertices.keys():
            if key == edge_one:
                self.vertices[key].add(edge_two)
            elif key == edge_two:
                self.vertices[key].add(edge_one)
        pass

