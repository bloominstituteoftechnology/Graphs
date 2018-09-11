"""
General drawing methods for graphs using Bokeh.
"""
import math
from graph import Graph
from node import Node
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    
    def show(self):
        N = len(self.graph.vertices)
        node_indices = list(range(N))

        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
                    tools='', toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(['black'] * N, 'color')
        graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color')

        graph.edge_renderer.data_source.data = dict(
            start=[0]*N,
            end=node_indices)

        ### start of layout code
        # circ = [i*2*math.pi/8 for i in node_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]
        x = [vertex.x for vertex in self.graph.vertices]
        y = [vertex.y for vertex in self.graph.vertices]
        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)

