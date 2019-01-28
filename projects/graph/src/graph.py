"""
Simple graph implementation
"""
"""
{
'0': {'1', '3'},
'1': {'0'},
'2': {set()},
'3': {'0'}
}
"""
import pprint

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, destination = None, label = None):
        self.vertices = {}
        self.edges = set()
        self.destination = destination
        self.label = label



    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        print(self.vertices)

    def add_edge(self, vertex_start, vertex_end):
        for i in self.vertices:
            # temp = set()
            # temp.add(i)
            if i == vertex_start:
                self.vertices[vertex_start].add(vertex_end)
                print(self.vertices)
            if vertex_end == i:
                self.vertices[vertex_end].add(vertex_start)
                print(self.vertices)


def print_vertex():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print("The Vertices: ",graph.vertices)
print_vertex()
