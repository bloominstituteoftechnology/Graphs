"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, numOne, numTwo):
        if numOne in self.vertices and numTwo in self.vertices:
            self.vertices[numOne].update(numTwo)
            self.vertices[numTwo].update(numOne)
        else:
            print('Those vertices do not exist')

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('4', '3')
# print(graph.vertices)