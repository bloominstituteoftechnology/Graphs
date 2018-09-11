"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex, edges=tuple()):
        self.vertices[vertex] = set(edges)
    def add_edge(self, head, tail):
        if head in self.vertices and tail in self.vertices:
            self.vertices[head].add(tail)
            self.vertices[tail].add(head)
        else:
            raise IndexError("One or more of these vertices does not exist!")

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)