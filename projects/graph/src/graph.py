"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
           self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        if vertex not in self.vertices or edge not in self.vertices:
            print('not found')
        else:
            self.vertices[vertex].add(edge)
            self.vertices[edge].add(vertex)


class Vertex:
    def __init__(self, vertex, x=None, y=None):
        self.id = vertex
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

        
thegraph = Graph()
thegraph.add_vertex('0')
thegraph.add_vertex('1')
thegraph.add_vertex('2')
thegraph.add_vertex('3')
thegraph.add_edge('0', '1')
thegraph.add_edge('0', '3')
print(thegraph.vertices)