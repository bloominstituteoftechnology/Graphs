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
        node_indices = list(self.graph.vertices)
        #x_value = [x for (x, y) in self.graph.vertices]
        #y_value = [y for (x, y) in self.graph.vertices]

        plot = figure(title="Graph Layout", x_range=(-2, 10),
                      y_range=(-2, 10), tools="", toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Circle(radius=0.3, fill_color='color')

        #print("\n x value: ", x_value)
        #print("\n y value: ", y_value)

        
        start_indices = []
        end_indices = []

        for vertex_id in self.graph.vertices:
            for edge_end in self.graph.vertices[vertex_id].edges:
                start_indices.append(vertex_id)
                end_indices.append(edge_end)

        graph.edge_renderer.data_source.data = dict(
            start=start_indices, end=end_indices)

        grid = [int(i) for i in self.graph.vertices]
        x = [self.graph.vertices[node].x for node in self.graph.vertices]
        y = [self.graph.vertices[node].y for node in self.graph.vertices]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')
        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)

