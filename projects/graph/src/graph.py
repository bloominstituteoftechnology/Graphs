#!/usr/bin/python
from collections import defaultdict

"""
Simple graph implementation compatible with BokehGraph class.
"""

# After seeing examples and reading docs, the following is not needed.
# class Vertex:
#   """Vertices have a 'label' and a set of edges"""
#     def __init__(self, label):
#         self.label = label
#         self.edges = set()

#     def __repr__(self):
#       retun str(self.label)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end, bidirectional=True):
        """Add a 'line' that runs from point to point"""
        pass

    def add_vertex(self, vertex, edges=()):
        """Add a 'point' that the 'edge/line' will run between"""
        pass


def main():
    pass


if __name__ == "__main__":
    main()
