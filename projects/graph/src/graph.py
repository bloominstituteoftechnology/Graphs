"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        if vertex not in self.verticies:
            self.verticies[vertex] = set()

    def add_edge(self, vertex, edge):
        if vertex not in self.verticies or edge not in self.verticies:
            print("not found")
        else:
            self.verticies[vertex].add(edge)
            self.verticies[edge].add(vertex)


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_edge('0', '1')
graph.add_vertex('2')
print(graph.verticies)