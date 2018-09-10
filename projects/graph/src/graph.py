"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.field = {}
    def add_vertex(self,v):
        self.field[v] = set()
    def add_edge(self,v,e):
        if not self.field[v]:
            raise ValueError('this vertex value is not available. please add it first')
        else:
            self.field[v].add(e)
    def vertices(self):
        return self.field

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices())
graph.add_edge('13','5')