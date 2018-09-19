"""
Simple graph implementation compatible with BokehGraph class.
"""
vertice_list = {
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}


class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color="white"):
        self.id = vertex_id
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()

        if self.x is None:
            self.x = self.id
        if self.y is None:
            self.y = self.id
        if self.value is None:
            self.value = self.id


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist")


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
