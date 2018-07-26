#!/usr/bin/python
# import numpy as np
import random
from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """Represent a vertex with a label and possible connected component."""

    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices."""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """Add a edge (default bidirectional) between two vertices."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS."""
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            quack.extend(self.vertices[current] - visited)

        return visited

    def find_components(self):
        """Identify components and update vertex component ids."""
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component


# class ListGraph:
#     """Adjacency list graph."""

#     def __init__(self):
#         self.vertices = set()

#     def add_edge(self, start, end, bidirectional=True):
#         """Add an edge from start to end."""
#         if start not in self.vertices or end not in self.vertices:
#             raise Exception("Error - vertices not in graph!")
#         start.edges.add(end)
#         if bidirectional:
#             end.edges.add(start)

#     def add_vertex(self, vertex):
#         if not hasattr(vertex, "label"):
#             raise Exception("This is not a vertex!")
#         self.vertices.add(vertex)

#     def bfs(self, start):
#         random_color = '#' + \
#             ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#         queue = []
#         found = []
#         queue.append(start)
#         found.append(start)

#         start.color = random_color

#         while (len(queue) > 0):
#             v = queue[0]
#             for edge in v.edges:
#                 if edge not in found:
#                     found.append(edge)
#                     queue.append(edge)
#                     edge.color = random_color

#             queue.pop(0)  # TODo look at collections.stack
#         return found

#     def dfs(self, start):
#         random_color = '#' + \
#             ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#         stack = []
#         found = []
#         stack.append(start)
#         found.append(start)

#         start.color = random_color

#         while (len(stack) > 0):
#             v = stack[len(stack) - 1]
#             for edge in v.edges:
#                 if edge not in found:
#                     found.append(edge)
#                     stack.append(edge)
#                     edge.color = random_color

#             stack.pop()  # TODo look at collections.stack
#         return found

#     # Get the connected components
#     def get_connected_components(self):
#         # Connected Components
#         # Go to the next unfound vertex in graph vertices and call BFS on it
#         # Go to step 1 until we get to the end of the array(loop)

#         searched = []

#         for index, vertex in self.vertices.items():
#             if vertex not in searched:
#                 searched.append(self.bfs(vertex))  # using bfs

#         return searched


# """
# General drawing methods for graphs using Bokeh.
# """
# # Random Graph
# # adj = np.random.randint(0,2,(n,n))
# # n = np.random.randint(1, N+1)
