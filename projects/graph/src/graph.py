#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """Object representation of Vertex"""
    def __init__(self, label=name):
        self.label = label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional = True):
        self.vertices[start].add(end)
        
        if bidrectional:
            self.vertices[end].add(start)

def main():
    graph = Graph()
    vertex0 = vertex('0')
    graph.add_vertex(vertex_0)
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

    if __name__ == '_main_':
        main()

