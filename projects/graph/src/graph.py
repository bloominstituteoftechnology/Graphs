class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')

        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

graph = Graph()  # Instantiate your graph
v0 = Vertex(0)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
graph.add_vertex(v0)
graph.add_vertex(v1)
graph.add_vertex(v2)
graph.add_vertex(v3)
graph.add_vertex('5')
graph.add_edge(v0, v1)
graph.add_edge(v0, v3)
graph.add_edge(v0, '5')
print(graph.vertices)

