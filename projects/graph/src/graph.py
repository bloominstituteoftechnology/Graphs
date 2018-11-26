"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex2 not in self.vertices:
            print('The vertex you are looking for does not exhist')
        else:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)

class Vertex:
    def __init__(self, unique_id, value, color):
        self.unique_id = unique_id
        self.value = value
        self.color = color

graph = Graph() 
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)