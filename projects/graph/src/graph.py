"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, value):
        self.verticies[value] = set()

    def add_edge(self, value1, value2):
        val = self.verticies[value1]
        val.add(value2)
        self.verticies[value1] = val
        val2 = self.verticies[value2]
        val2.add(value1)
        self.verticies[value2] = val2


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.verticies)
