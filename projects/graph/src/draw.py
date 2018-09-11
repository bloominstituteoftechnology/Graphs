"""
General drawing methods for graphs using Bokeh.
"""

import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet
from bokeh.palettes import Spectral8
from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = Graph()

    def show(self):
        node_indices = list(self.graph.vertices.keys())
        x_value = [x for (x, y) in self.graph.vertices.items()]
        y_value = [list(y) for (x, y) in self.graph.vertices.items()]

        plot = figure(title="Graph Layout", x_range=(-10, 30),
                      y_range=(-10, 30), tools="", toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(x_value, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Circle(radius=1.1, fill_color='color')

        print("\n x value: ", x_value)
        print("\n y value: ", y_value)

        graph.edge_renderer.data_source.data = dict(
            start=x_value, end=y_value)

        grid = [int(i) for i in x_value]
        x = [i for i in grid]
        y = [2 * (i % 5) for i in grid]

        graph_layout = dict(zip(x_value, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')
        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)

