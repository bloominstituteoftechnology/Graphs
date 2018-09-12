"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertix):
        self.vertices[str(vertix)] = set()
    def add_edge(self, start, end):
        start = str(start)
        end = str(end)
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertex does not exist!')
        else:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
    def add_directed_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].edges.add(end)
        else:
            raise IndexError("That vertex does not exist!")
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
