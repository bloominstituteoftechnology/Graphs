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
        
thegraph = Graph()
thegraph.add_vertex('0')
thegraph.add_vertex('1')
thegraph.add_vertex('2')
thegraph.add_vertex('3')
thegraph.add_edge('0', '1')
thegraph.add_edge('0', '3')
print(thegraph.vertices)