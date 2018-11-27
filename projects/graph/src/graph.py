"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.edges = set()

    def __repr__(self):
        return f"Edges: {self.edges}"


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return f"{self.vertices}"

    def add_vertex(self, name, value):
        vertex = Vertex(value)
        self.vertices[name] = vertex

    def add_edge(self, vertex_name, edge):
        self.vertices[vertex_name].edges.add(edge)

    def get_vert(self, name):
        return {name: self.vertices.get(name)}


g = Graph()
g.add_vertex("Cramerton", set)
g.add_vertex("McAdenville", set)
g.add_edge("Cramerton", "McAdenville")
g.add_edge("McAdenville", "Cramerton")
g.add_edge("McAdenville", "Lowell")
print(g)
print(g.get_vert("McAdenville"))

