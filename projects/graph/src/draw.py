"""
General drawing methods for graphs using Bokeh.
"""
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral4


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title="Graph", x_min=0, x_max=10, y_min=0, y_max=10):
        self.graph = graph
        self.title = title
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def show(self):
        node_indices = list(self.graph.vertices.keys())
        print(f"node_indices: ${node_indices}")

        start_vertices = []
        end_vertices = []

        for vertex, endpoints in self.graph.vertices.items():
            for end in endpoints:
                  start_vertices.append(vertex)
                  end_vertices.append(end)

        color_values = [color for (vertex, color) in self.graph.colors.items()]
        x_positions = [x for (vertex, x) in self.graph.x_positions.items()]
        y_positions = [y for (vertex, y) in self.graph.y_positions.items()]

        plot = figure(title=self.title, x_range=(self.x_min, self.x_max),
                      y_range=(self.y_min, self.y_max), tools="", toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(color_values, 'color')
        graph.node_renderer.glyph = Circle(radius=0.2, fill_color='color')

        graph.edge_renderer.data_source.data = dict(
            start=start_vertices, end=end_vertices)

        graph_layout = dict(zip(node_indices, zip(x_positions, y_positions)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('index.html')
        show(plot)