#!/usr/bin/python
"""Graph representation using adjacency list."""
from random import choice, random
from draw import BokehGraph
class Vertex:
    """ Vertices always have a label and a set of edges. """
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)

class Graph:    
    """ Represent a graph as a dictionary of vertices mapping labels to edges. """
    """ Type of graph: adjacency list """
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end, bidirectional=True):
        """ Adding an edge from start to end. """
        if start not in self.vertices or end not in self.vertices:
            raise Exception("%s or %s does not exist" %(start, end))
        else:
            self.vertices[start].add(end)
            if bidirectional == True:
                self.vertices[end].add(start)

    def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex]=set(edges)

    def randomize(self, grid_x=5, grid_y=4, jitter=150, edge_prob=0.6):
        #graph=self.Graph()
        for i in range(20): #0 to 19
            string=str(i)
            self.add_vertex(string)
        for vertex in self.vertices:
            for vertex1 in self.vertices:
                decision=random()
                if decision <= edge_prob:
                    self.add_edge(vertex,vertex1)
        bg=BokehGraph(self)
        bg.show()



        """if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError("That vertex already exists in the graph.")
"""

"""
graph = Graph()  # Instantiate your graph
v0=Vertex('V 0')
graph.add_vertex('0')
v1=Vertex('V 1')
graph.add_vertex('1')
v2=Vertex('V 2')
graph.add_vertex('2')
v3=Vertex('V 3')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
#graph.add_edge('0', '21')
print(graph.vertices)
"""