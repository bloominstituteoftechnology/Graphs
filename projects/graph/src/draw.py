import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Circle
from bokeh.palettes import Spectral8
from graph import Graph




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
        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color="red")

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

        output_file('graph.html')
        show(plot)




graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')


bg = BokehGraph(graph)
bg.draw()




#
# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import (GraphRenderer, Diamond, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource, Diamond)
# from graph import Graph
# from bokeh.models.glyphs import Oval
# import random
#
# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#
#     def __init__(self, graph):
#         self.graph = graph
#         self.graph_data = self.graph.vertices
#         self.edge_x = []
#         self.edge_y = []
#         self.node_x = []
#         self.node_y = []
#
#
#     def create_edge_lists(self):
#         for key in self.graph_data:
#             for val in self.graph_data[key]:
#                 self.edge_x.append(key)
#                 self.edge_y.append(val)
#
#     def create_node_locations(self):
#         for i in range(len(self.graph_data)):
#             x_val = random.randint(-len(self.graph_data), len(self.graph_data))
#             y_val = random.randint(-len(self.graph_data), len(self.graph_data))
#             self.node_x.append(x_val)
#             self.node_y.append(y_val)
#
#
#     def draw(self):
#         self.create_edge_lists()
#         self.create_node_locations()
#         v_len = len(self.graph_data)
#         plot = figure(title="Lil Sumpin", x_range=(-v_len-5, v_len+5), y_range=(-v_len-5, v_len+5), tools='', toolbar_location=None)
#
#         graphR = GraphRenderer()
#         graphR.node_renderer.data_source.add(self.edge_x, 'index')
#         graphR.node_renderer.glyph = Circle(radius=0.5, fill_color="red")
#         graphR.edge_renderer.data_source.data = dict(
#             start=self.edge_x,
#             end=self.edge_y)
#
#         graph_layout = dict(zip(self.graph_data.keys(), zip(self.node_x, self.node_y)))
#         print(graph_layout)
#         graphR.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
#         plot.renderers.append(graphR)
#
#         show(plot)
#         output_file('graph.html')
#
#
#
