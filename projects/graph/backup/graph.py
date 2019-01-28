"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vert_a, vert_b):
        if vert_a in self.vertices and vert_b in self.vertices:
            self.vertices[vert_a].add(vert_b)
        else:
            return 'exception occoured, one of the vertices is not in the Graph yet'

# graph = Graph()
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
