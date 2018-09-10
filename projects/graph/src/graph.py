"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, node):
        self.vertices[node] = set()
    def add_edge(self, node, neighbor):
        if node not in self.vertices or neighbor not in self.vertices:
            raise Exception('Error: Vertex does not exist')
        elif self.vertices[node] != set():
            self.vertices[node].add(neighbor)
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
#graph.add_edge('1', '4')
print(graph.vertices)
