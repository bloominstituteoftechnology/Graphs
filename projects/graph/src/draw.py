import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource
from bokeh.palettes import Spectral8
from graph import Graph


class BokehGraph:
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graph = self.graph
    
        N = len( graph.vertices )
        node_indices = list(graph.vertices.keys())

        print(node_indices)

        plot = figure(title="Graph Demonstration", x_range=(-7,7), y_range=(-7,7), tools="", toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        # node_colors = ['blue'] * N
        # graph_renderer.node_renderer.data_source.add(node_colors, 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.1, fill_color='blue')

        graph_renderer.edge_renderer.data_source.data = dict(
            start=[0]*N,
            end=node_indices)
        d = dict(
            start=[0]*N,
            end=node_indices)
        print(d)

        ### start of layout code
        x = []
        y = []
        for vertex_id in node_indices:
            vertex = graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        output_file('test_graph.html')
        show(plot)

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '3')
graph.add_edge('0', '1')

bg = BokehGraph(graph)
bg.draw()



