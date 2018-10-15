"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.graph = dict()

    def add_vertex(self, vert):
        if vert not in self.graph.keys():
            self.graph[vert] = set()

    def add_edge(self, start, end):
        if start in self.graph.keys():
            self.graph[start].add(end)

    def get_graph(self):
        return self.graph
