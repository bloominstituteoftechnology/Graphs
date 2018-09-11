"""
General drawing methods for graphs using Bokeh.
"""
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        self.graph = graph

    def show(self):

        node_indices = [k for (k, v) in self.graph.vertices.items()]
        edge__start = [k for (k, v) in self.graph.vertices.items()]
        edge__end = [list(v) for (k, v) in self.graph.vertices.items()]

        print("\n grap vertices: ", self.graph.vertices)
        print("\n edge__start: ", edge__start)
        print("\n edge__end: ", edge__end)

        N = len(edge__start)
        plot = figure(title="Graph Layout", x_range=(-1, 10),
                      y_range=(-2, 10), tools="", toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')

        graph.node_renderer.data_source.add(
            ['red'] * (N), 'color')
        graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color')

        start_i = []
        end_i = []
        for vertex in self.graph.vertices:
            for end_point in self.graph.vertices[vertex]:
                start_i.append(vertex)
                end_i.append(end_point)

        graph.edge_renderer.data_source.data = dict(
            start=start_i, end=end_i)

        x = [int(i) for i in node_indices]
        y = [math.sin(int(i)) for i in node_indices]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
        # print(graph_layout)
        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)
