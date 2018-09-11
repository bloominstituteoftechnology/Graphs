"""
General drawing methods for graphs using Bokeh.
"""

import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import Graph


class BokehGraph:
    def __init__(self, graph):
        self.graph = graph

    def show(self):
        node_indices = list(self.graph.vertices)
        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1, 10.1), y_range=(-1.1, 10.1), tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add(Spectral8, 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex in self.graph.vertices:
            for edge_end in self.graph.vertices[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge_end)
                graph_renderer.edge_renderer.data_source.data = dict(start=start_indices, end=end_indices)

         # start of layout code
        grid = [int(v) for v in self.graph.vertices]
        x = [2 * (i // 3) for i in grid]
        y = [2 * (i % 3) for i in grid]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)


graph = Graph()
bokeh = BokehGraph(graph)
bokeh.graph.add_vertex('0')
bokeh.graph.add_vertex('1')
bokeh.graph.add_vertex('2')
bokeh.graph.add_vertex('3')
bokeh.graph.add_edge('0', '1')
bokeh.graph.add_edge('0', '3')
bokeh.show()