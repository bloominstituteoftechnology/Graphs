"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, v1, v2):
        if v1 is in vertices and v2 is in vertices:
            self.vertices[v1].add[v2]
            self.vertices[v2].add[v1]
        else: 
            print("At least one vertex does not exist.")


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)