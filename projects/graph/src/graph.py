"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {
            "A": {"B", "C"},
            "B": {"A"},
            "C": {"B"}
        }
    def add_vertex(self, name):
        self.vertices[name] = set()

    def add_edge(self, vertex1, vertex2):
        self.vertices[vertex1].add(vertex2)
        
lilgraph = Graph()
lilgraph.add_vertex("D")
lilgraph.add_edge("D", "C")
lilgraph.add_edge("D", "B")
print(lilgraph.vertices)
