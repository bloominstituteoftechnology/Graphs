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

    def add_undirected_edge(self, start_edge, end_edge):
        if start_edge not in self.vertices:
            raise ValueError(f'Provided vertex {start_edge} does not exist')
        if end_edge not in self.vertices:
              raise ValueError(f'Provided vertex {end_edge} does not exist')
        self.vertices[start_edge].edges.add(end_edge)
        self.vertices[end_edge].edges.add(start_edge)

    def add_directed_edge(self, start_edge, end_edge):
        if start_edge not in self.vertices:
            IndexError(f'Vertex {start_edge} does not exist!')
        if end_edge not in self.vertices:
            IndexError(f'Vertex {end_edge} does not exist!')
        self.vertices[start_edge].edges.add(end_edge)    



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
