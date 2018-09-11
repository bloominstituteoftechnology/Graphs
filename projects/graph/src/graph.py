"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, label):
        if label in self.vertices:
            raise ValueError(f"Duplicate vertex'{label}' found")
        self.vertices[label] = set()
    def add_edge(self, label, target):
        if label not in self.vertices:
            raise ValueError(f"Vertex '{label}' not found")
        if target not in self.vertices:
            raise ValueError(f"Vertex '{target}' not found")
        self.vertices[label].add(target)