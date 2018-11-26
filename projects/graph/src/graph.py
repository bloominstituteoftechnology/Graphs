"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, value):
        self.node = value
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            vertex = Vertex(value)
            self.vertices[vertex.node] = vertex.edges
            return True
        else:
            return False

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
            return True
        else:
            if v1 not in self.vertices:
                raise IndexError(
                    f"Vertex {v1} is nonexistent!"
                )  # IndexError more specific than Exception
            elif v2 not in self.vertices:
                raise IndexError(f"Vertex {v2} is nonexistent!")


graph = Graph()
graph.add_vertex("0")
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_edge("0", "1")
graph.add_edge("0", "3")
graph.add_edge("0", "4")
print(graph.vertices)
