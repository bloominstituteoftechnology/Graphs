"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices={}

    def add_vertex(self, value):
        if value in self.vertices:
            raise ValueError(f'Duplicate vertex {value} found')
        self.vertices[value]=set()

    def add_edge(self, value, edge):
        if value not in self.vertices:
            raise ValueError(f'Provided vertex {value} does not exist')
        elif edge not in self.vertices:
              raise ValueError(f'Provided vertex {edge} does not exist')
        self.vertices[value].add(edge)






graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '4')
print(graph.vertices)
