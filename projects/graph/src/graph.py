"""
Simple graph implementation compatible with BokehGraph class.
"""

import random


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}

    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            raise ValueError(f'Duplicate vertex {value} found')
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, value, edge):
        if value not in self.vertices:
            raise ValueError(f'Provided vertex {value} does not exist')
        if edge not in self.vertices:
              raise ValueError(f'Provided vertex {edge} does not exist')
        self.vertices[value].edges.add(edge)



class Vertex:
    def __init__ (self, vertex_id, x=None, y=None, value=None, color="white"):
        self.id = int(vertex_id)
        self.edges = set()
        self.x = x
        self.y = y

        if x is None:
            self.x = random.random() * 10 - 5
        if y is None:
            self.y = random.random() * 10 - 5



'''graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
#graph.add_edge('0', '4')
print(graph.vertices)'''
