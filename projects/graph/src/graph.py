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
        if edge_one in self.vertices.keys() and edge_two in self.vertices.keys():
            self.vertices[edge_one].add(edge_two)
            self.vertices[edge_two].add(edge_one)
        else:
            raise KeyError
        # for key in self.vertices.keys():
        #     if key == edge_one and edge_two in self.vertices.keys():
        #     elif key == edge_two and edge_one in self.vertices.keys():
        pass

