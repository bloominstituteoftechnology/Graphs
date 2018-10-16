"""
General drawing methods for graphs using Bokeh.
"""

import random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                            ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    def show(self):
        node_indices = list(self.graph.vertices.keys())
        edges = [list(v) for v in self.graph.vertices.values()]

        plot = figure(title='Graph Layout Demonstration', x_range=(-1, 5), y_range=(-1, 5),
                      tools='', toolbar_location=None)
        plot.axis.visible = False
        plot.grid.visible = False

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Circle(size=20, fill_color='color')

        edge_start = []
        edge_end = []

        for vertex in self.graph.vertices:
            for edge in self.graph.vertices[vertex]:
                edge_start.append(vertex)
                edge_end.append(edge)

        graph.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)

        position = {}
        for vertex in self.graph.vertices:
            position[vertex] = (random.random() * 4, random.random() * 4)

        graph.layout_provider = StaticLayoutProvider(graph_layout=position)
        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
#
# bokeh_graph = BokehGraph(graph)
# bokeh_graph.show()
