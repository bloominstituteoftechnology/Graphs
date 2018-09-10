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
        else:
            raise Exception("This vertex has already been added")

    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
        else:
            raise Exception("One of your vertices doesn't exist")

# Test
graph = Graph()  
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_vertex('3')
print(graph.vertices)