"""
Simple graph implementation
"""
class Vertex:
    """Extracts the vertex from the graph, I think this way will scale better"""
    def __init__(self, vertex_val):
        self.vertex = vertex_val
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        pass  # TODO

    def add_vertex(self, vertex):
        new_vertex = Vertex(vertex)
        self.vertices[new_vertex.vertex] = new_vertex.edges

    def add_edge(self, edge_one, edge_two):
        if edge_one in self.vertices.keys() and edge_two in self.vertices.keys():
            self.vertices[edge_one].add(edge_two)
            self.vertices[edge_two].add(edge_one)
        else:
            raise IndexError("That vertex does not exist")
        pass

