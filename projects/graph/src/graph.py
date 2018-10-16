"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex
#         if not label in self.vertices:
#             self.vertices[label] = set()

#     def add_edge(self, vertex, destination):
#         if vertex in self.vertices and destination in self.vertices:
#             self.vertices[vertex].add(destination)
#             self.vertices[destination].add(vertex)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
# creates an empty graph

    def __init__(self):
        self.vertices = {}
        # creates an empty graph
# adds vertex to graph

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
        # adds vertex to graph

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist")
            # adds an edge to graph
# this also adds undirected edge

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist")
# adds a directed edge to the graph


class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x == None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y == None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
# creates an empty vvertex

    def __repr__(self):
        return f"{self.edges}"


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
print(graph.vertices)
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
