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

    def breadth_first_search(self, vertex):
        pass

    def __str__(self):
        return str(self.vertices)


lg = ListGraph()
#for x in range(0, 25):
 #   lg.add_vertex(Vertex(f"v {x}"))

v1 = Vertex("v 1")
lg.add_vertex(v1)
v2 = Vertex("v 2")
lg.add_vertex(v2)
v3 = Vertex("v 3") 
lg.add_vertex(v3)
v4 = Vertex("v 4")
lg.add_vertex(v4)
v5 = Vertex("v 5")
lg.add_vertex(v5)
v6 = Vertex("v 6")
lg.add_vertex(v6)
v7 = Vertex("v 7")
lg.add_vertex(v7)
v8 = Vertex("v 8")
lg.add_vertex(v8)

lg.add_edge(v1, v3, False)
lg.add_edge(v2, v1, False)
lg.add_edge(v3, v6, False)
lg.add_edge(v8, v3, False)
lg.add_edge(v7, v5, False)
lg.add_edge(v6, v8, False)

print(lg)
print(v1.edges)
