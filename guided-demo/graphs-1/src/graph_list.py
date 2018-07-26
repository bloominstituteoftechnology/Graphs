"""Graph representation using adjacency list."""

class Edge:
    """Edges in the adjacency list are just a destination."""
    # Using simple classes for illustrative purposes
    # pylint: disable=too-few-public-methods
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    """Vertices have a label and a set of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label
        self.edges = set()


class Graph:
    """The graph itself is simply a set of vertices."""
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.vertices = set()


'''
Simple graph implementation compatible with BokehGraph Class
'''
def __init__(self):
    self.vertices = {}
    
    def add_vertex(self, vertex, edges=()):
        #add a new vertex, optionally with edges to other vertices.
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: Cannot have edge to nonexistent vertices')
        if vertex in self.vertices:
            raise Exception("Error: Adding vertex that already exists")
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        #add an edge (default bidirectional) between two vertices.
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error: Vertices to connect not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)