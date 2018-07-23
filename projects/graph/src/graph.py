#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
"""
# from the lecture
# Vertices have a label and a set of edges.
class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()   #vertax = node, edges = pointers.  Set() helps to build the graph list

    #to make it easier to read. without it, it just prints the position index in memory
    def __repr__(self):
        return str(self.label)
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # represent as a dict

    def add_vertex(self, vertex):
        self.vertices[vertex] = set() 

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
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
# graph.add_edge('0', '4')
# graph.add_edge('a', '0')
# graph.add_edge('x', 'y')
print(graph.vertices)

