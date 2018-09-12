"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.edges = set()
        if self.x is None:
            self.x = 3 * (self.id // 3)
        if self.y is None:
            self.y = 3 * (self.id % 3)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def add_edge(self, vertex, edge):
        self.vertices[vertex].edges.add(edge)
        self.vertices[edge].edges.add(vertex)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)

