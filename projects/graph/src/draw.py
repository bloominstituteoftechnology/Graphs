import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider,ColumnDataSource, Oval, Circle, Label, LabelSet

from bokeh.palettes import Spectral8
from graph import Graph
import random



class BokehGraph:
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graph = self.graph

        N = len( graph.vertices )
        node_indices = list(graph.vertices.keys())

        plot = figure(title="Graph Layout Demonstration", x_range=(-7,7), y_range=(-7,7),
                      tools="", toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        # node_colors = ['red'] * N
        # graph.node_renderer.data_source.add(node_colors, 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.5, line_width=5, line_color="orange", fill_color="blue")

        edge_start = []
        edge_end = []

        # O(E), where E is the total number of edges
        for vertex_id in node_indices:
            for v in graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(v)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)

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

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[vertex_id for vertex_id in graph.vertices]))
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                     text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')


        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)

# graph = Graph()
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_vertex('5')
# graph.add_edge('0', '1')
# graph.add_edge('0', '2')
# graph.add_edge('1', '3')
# graph.add_edge('2', '4')
# graph.add_edge('3', '5')


# bg = BokehGraph(graph)
# bg.draw()