"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource, Oval)
from bokeh.palettes import Spectral4

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    def show(self):
        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools='', toolbar_location=None)

        graph = GraphRenderer()
    
        graph.node_renderer.data_source.add(list(self.graph.vertices.keys()), 'index')
        graph.node_renderer.data_source.add(Spectral4, 'color')
        graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

        graph.edge_renderer.data_source.data = dict(
        start=[0]*4,
        end=list(range(4)))

        plot.renderers.append(graph)

        graph.layout_provider = StaticLayoutProvider(
            graph_layout={3, 3})

        output_file('graph.html')
        show(plot)
