"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph=None, title='Simple Graph Title', w=5, h=5):
        self.graph = graph
        self.plot = figure(title=title, x_range=(0, w), y_range=(0, h))

    def setup_graph(self, circle_size=5):
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(self.vertices.keys(), 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Circle(size=circle_size, fill_color='color')
        graph.edge_renderer.data_source.data = dict(
            start = [],
            end = []
        )

        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

    def show_plot(self, output_path = './graph.html'):
        output_file(output_file)
        show(self.plot)
