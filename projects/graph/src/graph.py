#!/usr/bin/python

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
            raise ValueError("Error: Vertex already exists")
    
    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error: %s and/or %s do not exist" %(start, end))
        else:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)