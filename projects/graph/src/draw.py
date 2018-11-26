"""
General drawing methods for graphs using Bokeh.
"""

import random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    def show(self, connected=False):
        node_indices = list(self.graph.vertices.keys())

        plot = figure(title='Graph Layout Demonstration', x_range=(-1, 5), y_range=(-1, 5),
                      tools='', toolbar_location=None)
        plot.axis.visible = False
        plot.grid.visible = False

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')

        # Random color generator
        if connected:
            graph.node_renderer.data_source.add(node_indices, 'index')
            color = []
            for vertex in self.graph.vertices:
                color.append(self.graph.vertices[vertex].color)
        else:
            graph.node_renderer.data_source.add(node_indices, 'index')
            number_of_colors = len(node_indices)
            color = ["#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
                     for _ in range(number_of_colors)]

        graph.node_renderer.data_source.add(color, 'color')
        graph.node_renderer.glyph = Circle(size=20, fill_color='color')

        edge_start = []
        edge_end = []

        for vertex in self.graph.vertices:
            for edge in self.graph.vertices[vertex].edges:
                edge_start.append(vertex)
                edge_end.append(edge.name)

        graph.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)

        # TODO: Need to implement a way that nodes don't overlap, or are too close
        position = {}
        for vertex in self.graph.vertices:
            position[vertex] = (random.random() * 4, random.random() * 4)

        graph.layout_provider = StaticLayoutProvider(graph_layout=position)
        source = ColumnDataSource(dict(x=[x for x, y in position.values()], y=[y for x, y in position.values()], name=node_indices))
        labels = LabelSet(x='x', y='y', text='name', level='glyph',
                          x_offset=7, y_offset=7, source=source, render_mode='canvas')

        plot.add_layout(labels)
        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)
