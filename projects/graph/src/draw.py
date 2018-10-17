"""
General drawing methods for graphs using Bokeh.
"""
from graph import Graph
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graph = self.graph
        N = len(graph.vertices)
        node_indices = list(range(N))

        plot = figure(title="Graph Layout Demonstration", x_range=(-4, 4), y_range=(-4, 4),
                    tools="", toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.glyph = Circle(radius=0.25, fill_color='green')

        graph_renderer.edge_renderer.data_source.data = dict(
            start=[0]*N,
            end=node_indices)

        d = dict(
            start=[0]*N,
            end=node_indices)
        print('d is: ', d)

        ### start of layout code
        circ = [i for i in node_indices]
        x = [i for i in circ]
        y = [i for i in circ]
        
        
        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)


        plot.renderers.append(graph_renderer)

        output_file("graph.html")
        show(plot)
                
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)

bg = BokehGraph(graph)
bg.draw()