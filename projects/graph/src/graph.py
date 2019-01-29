"""
Simple graph implementation
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = {}
    
    def add_vertex(self, value):
        if not value in self.vertices:
            self.vertices[value] = set()
    
    def add_edge(self, vertex, target):
        # print(self.vertices)
        # print(self.vertices[vertex])
        # print(hasattr(self.vertices, vertex))
        if vertex in self.vertices and target in self.vertices:
            self.vertices[vertex].add(target)
        else:
            print('One of the provided vertices does not exist.')

# Test
graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '0')
graph.add_edge('3', '0')
print(graph.vertices)
graph.add_edge('0', '4')