"""
Simple graph implementation compatible with BokehGraph class.
"""

mygraph = {
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.value = value
    def add_edge(self, target):
        myg = nx.Graph(mygraph)
    def add_vertex(self, target):
        copy = self.copy()
        copy.update(target)
