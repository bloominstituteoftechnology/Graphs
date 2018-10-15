"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verts = {}
    
    def add_vertex(self, vert):
        self.verts[vert] = set()
    
    def add_edge(self, vert, edge):
        if vert in self.verts:
            self.verts[vert].add(edge)
        else:
            print(f"Vert {vert} does not exist")


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '3')
print(graph.verts)
