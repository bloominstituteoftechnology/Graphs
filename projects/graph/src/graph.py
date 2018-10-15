"""
Simple graph implementation compatible with BokehGraph class.
"""
from collections import defaultdict

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
       self.vertices = defaultdict(set)

    def add_edge(self, start, end, bidirectional = True):
           # Adding edge from start to end
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Sorry!!! Vertices are not in the graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()


graph = Graph()
graph.add_vertex("0")
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_edge("0", "1")
graph.add_edge("0", "3")
print(graph.vertices)
