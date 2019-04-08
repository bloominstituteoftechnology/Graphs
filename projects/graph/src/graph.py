"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def addVertex(self, num):
        if num not in self.vertices:
            self.vertices[num] = set()

    def addSingleEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)


    def addDoubleEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2].add(v1)
            self.vertices[v1].add(v2)

graph = Graph()  # Instantiate your graph
graph.addVertex('0')
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addDoubleEdge('0', '1')
graph.addDoubleEdge('0', '3')
print(graph.vertices)




