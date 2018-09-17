"""
Simple graph implementation compatible with BokehGraph class.
"""
vertice_list = {
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertice(self, vertice):
        self.vertices[vertice] = set()

    def add_edge(self, vertice1, vertice2):
        self.vertices[vertice1].add(vertice2)
        self.vertices[vertice2].add(vertice1)


graph = Graph()  # Instantiate your graph
graph.add_vertice('0')
graph.add_vertice('1')
graph.add_vertice('2')
graph.add_vertice('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
