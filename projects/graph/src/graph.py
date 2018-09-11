"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices={}):
        self.vertices = vertices
    def add_vertex(self, node):
        if isinstance(node, str):
            self.vertices[node] = set()
        elif isinstance(node, list):
            for i in node:
                self.vertices[i] = set()
    def add_edge(self, node, neighbor):
        if node not in self.vertices or neighbor not in self.vertices:
            raise Exception('Error: Vertex does not exist')
        elif self.vertices[node] != set():
            self.vertices[node].add(neighbor)
            self.vertices[neighbor] = {node}
        else:
            self.vertices[node] = {neighbor}
            self.vertices[neighbor] = {node}

    def add_edges(self, edges):
        for i, j in edges:
            if self.vertices[i] != set():
                self.vertices[i].add(j)
                self.vertices[j] = {i}
            else:
                self.vertices[i] = {j}
                self.vertices[j] = {i}
            


