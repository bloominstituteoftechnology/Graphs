"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {
                            '0': {'1', '3'},
                            '1': {'0'},
                            '2': set(),
                            '3': {'0'}
                        }
