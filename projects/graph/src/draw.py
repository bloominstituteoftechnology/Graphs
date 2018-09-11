

"""
General drawing methods for graphs using Bokeh.
"""
import math
from graph import graph
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource, Oval)
from bokeh.palettes import Spectral8


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        self.graph = graph

    def show(self):
        N = len(graph.vertices)
        node_indices = list(graph.vertices)
        plot = figure(title='Graph', x_range=(-2, 5), y_range=(-2, 5),
                      tools='', toolbar_location=None)
        graph_renderer = GraphRenderer()
        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add(
            ['red', 'blue', 'green', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'], 'color')
        graph_renderer.node_renderer.glyph = Circle(
            radius=0.2, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex in graph.vertices:
            for edge_end in graph.vertices[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge_end)
        graph_renderer.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)

        # start of layout code
        grid = [int(v) for v in graph.vertices]
        x = [2 * (i // 3) for i in grid]
        y = [2 * (i % 3) for i in grid]
        # x = [i for i in grid]
        # y = [i ** 2 for i in grid]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                          text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)


new_graph = BokehGraph(graph)
new_graph.show()
