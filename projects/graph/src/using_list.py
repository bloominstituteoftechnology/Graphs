"""Graph representation using adjacency list."""


class Vertex:
    """Vertices have a label and a set of edges."""
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)


class ListGraph:
    """Adjacency list graph."""
    def __init__(self):
        self.vertices = set()

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices.add(vertex)


graph = ListGraph()  # Instantiate your graph
v0=Vertex('V 0')
graph.add_vertex('0')
v1=Vertex('V 1')
graph.add_vertex('1')
v2=Vertex('V 2')
graph.add_vertex('2')
v3=Vertex('V 3')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
#graph.add_edge('0', '21')
print(graph.vertices)
