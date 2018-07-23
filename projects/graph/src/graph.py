#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices):
        self.matrix = [[0] * vertices] * vertices

    def add_edge(self, start, end, bidirectional=True):
        self.matrix[start][end] = 1
        if bidirectional:
            self.matrix[end][start] = 1
        

        pass  # TODO
