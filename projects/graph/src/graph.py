#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        vertex = Vertex(label)
        self.vertices[str(label)] = vertex.edges

    def add_edge(self, start_vertex, end_vertex, bidirectional=True):
        keys = self.vertices.keys()
        if (start_vertex not in keys) and (end_vertex not in keys):
            raise Exception('The vertex are not in the Graph')
        elif start_vertex not in keys:
            raise Exception(
                f'''The vertex {start_vertex} is not in the Graph.''')
        elif end_vertex not in keys:
            raise Exception(
                f'''The vertex {end_vertex} is not in the Graph.''')
        else:  # Both Vertex are in the Graph
            if bidirectional:
                self.vertices[str(start_vertex)].add(str(end_vertex))
                self.vertices[str(end_vertex)].add(str(start_vertex))
            else:
                self.vertices[str(start_vertex)].add(str(end_vertex))


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
graph.add_edge('0', '4')
