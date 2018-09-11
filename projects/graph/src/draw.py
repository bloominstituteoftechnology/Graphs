"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    def show(self):
        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
                    tools='', toolbar_location=None)
                    
        N = len(self.graph.vertices)
        node_indices = list(self.graph.vertices)

        graph = GraphRenderer()
    
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(['red'] * N, 'color')
        graph.node_renderer.glyph = Circle(radius=0.2, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex in self.graph.vertices:
            for edge in self.graph.vertices[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge)

        graph.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)

        grid = [int(v) for v in self.graph.vertices]
        x = [2 * (i // 3) for i in grid]
        y = [2 * (i % 3) for i in grid]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)
