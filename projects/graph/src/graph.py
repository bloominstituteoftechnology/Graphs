"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        pass  # TODO
    
    def add_vertex(self,value):
        self.vertices[value] = set()

    def add_edge(self, value, valuetwo):
        self.vertices[value].add(valuetwo)
        self.vertices[valuetwo].add(value)

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)