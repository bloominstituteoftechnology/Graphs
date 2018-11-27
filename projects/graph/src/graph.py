"""
Simple graph implementation compatible with BokehGraph class.
"""
# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component
        # self.edge = set()
    
    # def __str__(self):
    #     print(self.label)

    def __repr__(self):
        return 'Vertex: ' + self.label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, Vertex):
        self.vertices(Vertex) = set{}

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add[v2]
            self.vertices[v2].edges.add[v1]

    # def add_vertex(self, vertex, edges=()):
    #     if vertex in self.vertices:
    #         raise Exception('Error: trying to add a vertex that is already there!!!')
    #     if not set(edges).issubset(self.vertices):
    #         raise Exception('Error: trying to add an edge to no vertices?!?!?!')
    #     self.vertices[vertex] = set(edges)

    # def add_edge(self, start, end, bidirectional=True):
    #     if start not in self.vertices or end not in self.vertices:
    #         raise Exception('Vertices to connect not in graph')
    #     self.vertices[start].add(end)
    #     if bidirectional:
    #         self.vertices[end].add(start)
