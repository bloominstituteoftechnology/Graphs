#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""



class Graph:
    # Represent a graph as a dictionary of vertices mapping labels to edges.
    def __init__(self):
        self.vertices = {}  # represent as a dict

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('Error - adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error - cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges) 

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices to connect not in graph')
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
#graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
print(graph.vertices)

