"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import *


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__( self, graph, width=800, height=600, circle_size=30 ):
        if not graph.vertices:
            raise Exception("Graph should have vertices")
        self.graph = graph
        self.width = width 
        self.height = height
        self.pos = {}
        self.plot = figure(x_range=(0, width), y_range=(0, height))
        self._setup_graph_renderer(circle_size)
    
    def _setup_graph_renderer(self, circle_size):
        graph_render = GraphRenderer()

        graph_render.node_render.data_sorce.add(list(self.graph.vertices.keys()), "index")
        graph_render.node_render.data_sorce.add(Spectral8, 'color')
        graph_render.node_render.glyph = Circle(size=circle_size, fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)
