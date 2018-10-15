"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph

g = Graph()
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_edge('0', '1')
g.add_edge('0', '2')
g.add_edge('0', '3')

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.vertices = graph.vertices
        self.size = len(graph.vertices)

    def show(self):
        node_indices = list(range(self.size))
        plot = figure(title='graph_demo', x_range = (-1.1, 5.1), y_range = (-1.1, 5.1), tools="", toolbar_location=None)
        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices,'index')
        graph.node_renderer.data_source.add(['green'], 'color')
        graph.node_renderer.glyph = Circle(radius=0.5, fill_color='color')
        graph.edge_renderer.data_source.data = dict(
            start=[0]*self.size,
            end=node_indices)

        circ = [int(v) for v in g.vertices]
        x = [2 * (i // 3) for i in circ]
        y = [2 * (i % 3) for i in circ]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)
        output_file('graph.html')
        show(plot)

bg = BokehGraph(g)
bg.show()