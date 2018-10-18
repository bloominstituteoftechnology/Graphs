"""
General drawing methods for graphs using Bokeh.
"""
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource, Oval)
from bokeh.palettes import Spectral8

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    def show(self):
        graph = self.graph
        N = len( self.graph.vertices )
        # node_indices = 4
        node_indices = list(self.graph.vertices.keys())

        plot = figure(title="Mike Kerbleski Graph", x_range=(0,10.1), y_range=(0,10.1),
              tools="", toolbar_location=None)

        graph_renderer = GraphRenderer()
        

        edge_start = []
        edge_end = []

        # print(node_indices)

        for vertex_id in node_indices:
            for v in graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(v)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start, 
            end=edge_end
        )

        x = []
        y = []

        colors = []
        color1 = "red"
        color2 = "blue"


        for vertex_id in node_indices:
            if vertex_id in edge_start:
                colors.append(color1)
            else: 
                colors.append(color2)

            #CHECK FOR CONNECTION ON VERTEX_Id
            #IF IT ADD color1 to colors
            #IF NOT ADD color2 to colors 
            #that gives the right amount of colors

            vertex = graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)
            

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add(colors, 'color')
        graph_renderer.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color="color")

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        ### Draw quadratic bezier paths
        def bezier(start, end, control, steps):
            return [(1-s)**2*start + 2*(1-s)*s*control + s**2*end for s in steps]

        plot.renderers.append(graph_renderer)

        output_file("graph.html")
        show(plot)