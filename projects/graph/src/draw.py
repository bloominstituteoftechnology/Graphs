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
        self.width = width
        self.height = height
        self.node_indices = list(graph.vertices.keys())
        self.plot = figure(title='Graph', x_range=(0, width),
                           y_range=(0, height), tools='',
                           toolbar_location=None)
        self.renderer = GraphRenderer()

    def make_graph(self):
        self.renderer.node_renderer.data_source.add(self.node_indices, 'index')
        self.renderer.node_renderer.glyph = Circle(size=30, fill_color='color')
        self.connect_nodes()
        self.renderer.edge_renderer.data_source.data = self.graph.get_edges()
        self.renderer.node_renderer.data_source.add(list(self.graph.get_colors()),
                                                    'color')
        graph_layout = dict(
            zip(self.node_indices, list(self.graph.get_nodes())))
        self.renderer.layout_provider = (
            StaticLayoutProvider(graph_layout=graph_layout))
        self.plot.renderers.append(self.renderer)
        output_file('graph.html')
        show(self.plot)

    def connect_nodes(self):
        connected = set()
        base_x = self.width / 2
        base_y = self.height / 2
        mod_x = 1
        mod_y = 1
        count = 1
        for node in self.graph.vertices:
            if self.graph.vertices[node] not in connected:
                connected_nodes = (
                    self.graph.search(node,
                                      base_x + mod_x,
                                      base_y + mod_y))
                connected |= connected_nodes
                mod_x += (mod_x * -1) + (
                    (self.width / len(self.graph.vertices))) * count
                mod_y += (mod_y * -1) + (
                    (self.height / len(self.graph.vertices))) * count
                count += 1
