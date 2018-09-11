"""
Simple graph implementation compatible with BokehGraph class.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource, Oval)
from bokeh.palettes import Spectral8


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError(f'There is already a vertex {vertex} here')

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise IndexError(f"There's not vertex there to add an edge to!")
        else:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)

    def add_directed_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
        else:
            raise IndexError("That vertex does not exist")


"""def dft(adjList, vertex):
    print(vertex)
    for child_node in adjList[vertex]:
        dft(adjList, child_node)"""


def dft(adjList, vertex, visited):
    print(vertex)
    visited.append(vertex)
    for child_node in adjList[vertex]:
        if child_node not in visited:
            dft(adjList, child_node, visited)


def dfs(adjList, vertex, search_node):
    has_search = False

    def inner_dfs(adjList, vertex, search_node):
        nonlocal has_search
        if vertex == search_node:
            has_search = True
        for child_node in adjList[vertex]:
            inner_dfs(adjList, child_node, search_node)
    inner_dfs(adjList, vertex, search_node)
    return has_search


def bft(adjList, node_id):
    frontier = []
    frontier.append(node_id)
    while len(frontier) > 0:
        n = frontier.pop()
        print(n)
        for next_node in adjList[n]:
            frontier.append(next_node)


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_directed_edge('0', '1')
graph.add_directed_edge('0', '3')

graph.add_directed_edge('1', '2')
graph.add_directed_edge('2', '5')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '7')
graph.add_directed_edge('3', '6')
# graph.add_edge('0', '4')
print(graph.vertices)
# print(dfs(graph.vertices, '0', [], '8'))  # False, we're not connected to 8.
print(dfs(graph.vertices, '0', '9'))  # True.
