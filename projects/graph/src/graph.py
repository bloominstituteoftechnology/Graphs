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


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
# graph.add_edge('0', '4')
print(graph.vertices)
