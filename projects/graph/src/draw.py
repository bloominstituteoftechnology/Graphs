"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph

class BokehGraph:
    def __init__(self, graph):
        self.graph = graph

    def show(self):
        graph = self.graph
        N = len(graph.vertices)
        node_indices = list(graph.vertices.keys())
        plot = figure(title='graph_demo', x_range = (-5, 5), y_range = (-5, 5), tools="", toolbar_location=None)

        graph_renderer = GraphRenderer()
        graph_renderer.node_renderer.data_source.add(node_indices,'index')
        graph_renderer.node_renderer.glyph = Circle(radius=0.25, fill_color='green')

        edge_start = []
        edge_end = []
        for vertex_id in node_indices:
            for v in graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(v)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)

        x = []
        y = [1,3,5,2]
        for vertex_id in node_indices:
            vertex = graph.vertices[vertex_id]
            x.append(int(vertex.id))

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)
        output_file('graph.html')
        show(plot)

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
# graph.add_edge('0', '2')
graph.add_edge('0', '3')

bg = BokehGraph(graph)
bg.show()