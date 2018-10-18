"""
General drawing methods for graphs using Bokeh.
"""
import math
from graph import Graph
from bokeh.io import show, output_file, show
from bokeh.plotting import figure, output_file, show
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, Oval,
                          ColumnDataSource)
# from bokeh.palettes import Spectral8

class BokehGraph():
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graph = self.graph

        N = len(graph.vertices)
        node_indices = list(graph.vertices.keys())

        print(f"node indices: {node_indices}")

        plot = figure(title='Graph Layout Demonstration', x_range=(-10,10), y_range=(-10,10),
                    tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        # graph.node_renderer.data_source.add(Spectral8, 'color')
        graph_renderer.node_renderer.glyph = Oval(height=0.6, width=0.5, fill_color='red')

        graph_renderer.edge_renderer.data_source.data = dict(
            start=[0]*N,
            end=node_indices)

        d = dict(
            start=[0]*N,
            end=node_indices
        )
        print(f"dict: {d}")

        ### start of layout code
        # circ = [i*2*math.pi/8 for i in node_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]
        x = []
        y = []
        for vertex_id in node_indices:
            vertex = graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        output_file('graph.html')
        show(plot)



# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)

# bg = BokehGraph(graph)
# bg.draw()