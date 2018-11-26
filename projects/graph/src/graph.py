"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # store vertices in dictionary
        self.vertices = {}

graph = Graph()  # Instantiate your graph
print(graph.vertices)