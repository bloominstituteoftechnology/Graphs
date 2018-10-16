"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle,
                          LabelSet, ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph, height, width):
        self.graph = graph
        self.node_indices = list(graph.vertices.keys())
        self.plot = figure(title='Graph', x_range=(0, width),
                           y_range=(0, height), tools='',
                           toolbar_location=None)
        self.renderer = GraphRenderer()

    def make_graph(self):
        self.renderer.node_renderer.data_source.add(self.node_indices, 'index')
        self.renderer.node_renderer.glyph = Circle(size=30, fill_color='red')

        self.renderer.edge_renderer.data_source.data = self.graph.get_edges()
        graph_layout = dict(
            zip(self.node_indices, list(self.graph.get_nodes())))
        self.renderer.layout_provider = (
            StaticLayoutProvider(graph_layout=graph_layout))
        self.plot.renderers.append(self.renderer)
        output_file('graph.html')
        show(self.plot)
