#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vert:
    def __init__(self, label):
        self.label = label
        self.edges = set()
        self.pos = pos
        self.color = color

    def __repr__(self):
        return str(self.label, self.color, self.edges)


# class Graph:
#     """Represent a graph as a matrix of vertices mapping labels to edges."""

#     def __init__(self, num_vertices):
#         self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
#         self.vertices = [Vert(str(i)) for i in range(num_vertices)]

#     def add_edge(self, x_pos, y_pos, is_bidirectional=True):
#         """adds edges to graph"""
#         self.matrix[x_pos][y_pos] = 1
#         if is_bidirectional:
#             self.matrix[y_pos][x_pos] = 1


# todo
# Get current working graph class to represent it in a list.
class DictGraph:
    """Represent a graph as a dictionary of verts mapped to edges"""

    def __init__(self):
        self.verts = set()

    def add_edge(self, start, end, is_bidirectional=True):
        start.edges.add(end)
        if is_bidirectional:
            end.edges.add(start)

    def add_vert(self, vert):
        self.verts.add(vert)
