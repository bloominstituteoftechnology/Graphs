"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource, Diamond)
from graph import Graph
from bokeh.models.glyphs import Oval
import random

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        self.graph = graph
        self.graph_data = self.graph.vertices
        self.edge_x = []
        self.edge_y = []
        self.node_x = []
        self.node_y = []


    def create_edge_lists(self):
        for key in self.graph_data:
            for val in self.graph_data[key]:
                self.edge_x.append(key)
                self.edge_y.append(val)

    def create_node_locations(self):
        for i in range(len(self.graph_data)):
            x_val = random.randint(0,len(self.graph_data))
            y_val = random.randint(0, len(self.graph_data))
            self.node_x.append(x_val)
            self.node_y.append(y_val)
        return

    def draw(self):
        self.create_edge_lists()
        self.create_node_locations()
        # create plot = figure
        v_len = len(self.graph_data)
        plot = figure(title="Lil Sumpin", x_range=(-v_len-3, v_len+3))

        # create GraphRenderer
        graphR = GraphRenderer()

        # apply render nodes to graph
        graphR.node_renderer.data_source.add(self.node_x, 'index')
        graphR.node_renderer.data_source.add('black', 'color')
        graphR.node_renderer.glyph = Oval(height=0.5, width=0.4, fill_color='color')

        # apply render edges to graph
        graphR.edge_renderer.data_source.data = dict(
            start=self.edge_x,
            end=self.edge_y)

        graph_layout = dict(zip(self.edge_x, zip(self.node_x, self.node_y)))

        graphR.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graphR)

        output_file('graph.html')
        show(plot)



g = Graph()  # Instantiate your graph
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_edge('0', '1')
g.add_edge('0', '3')
g.add_edge('2', '3')
g.add_edge('5', '2')
g.add_edge('6', '1')
g.add_edge('4', '6')
g.add_edge('1', '6')
print(g.vertices)

bok = BokehGraph(g)
bok.draw()

