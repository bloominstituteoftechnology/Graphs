"""
Simple graph implementation
"""
#initial commit

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # add a dictionary of vertices
        self.vertices = {}
    # placeholders for add_vertex and add_edge methods
    # add_vertex needs only a vertex, while add_edge needs both a vertex and edge
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)

# testing

graph = Graph() 
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)