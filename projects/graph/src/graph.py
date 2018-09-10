"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, node):
        self.vertices[node] = {}
    def add_edge(self, node, neighbor):
        if self.vertices[node] != {}:
            tmp = {
                node: {neighbor}
            }
            {i:j for i in self.vertices.keys() for j in zip(self.vertices.values(), tmp.values())}
                #self.vertices[node] = {neighbor}
            self.vertices[neighbor] = {node}
        else:
            self.vertices[node] = {neighbor}
            self.vertices[neighbor] = {node}
            


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
