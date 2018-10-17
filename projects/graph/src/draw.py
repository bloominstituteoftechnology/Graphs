"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet,ColumnDataSource,Oval
from bokeh.palettes import Spectral8
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self,graph):
        self.graph=graph
    def draw(self):
        graph=self.graph
        N = 8
        node_indices = list(range(N))

        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),tools='', toolbar_location=None)
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')
        graph.edge_renderer.data_source.data = dict(
            start=[0]*N,
            end=node_indices)

        circ = [i*2*math.pi/8 for i in node_indices]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')

bg=BokehGraph(graph)
bg.draw()