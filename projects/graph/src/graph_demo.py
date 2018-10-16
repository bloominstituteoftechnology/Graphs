"""
General drawing methods for graphs using Bokeh.
"""
import math
import random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Circle
from bokeh.palettes import Spectral8
from graph import Graph
class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graph = self.graph
        N = len(graph.vertices)
        node_indices = list(graph.vertices.keys())
        plot = figure(title='graph_demo', x_range = (-1, 10), y_range = (-1, 10), tools="", toolbar_location=None)
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
        axis = {}
        for vertex in self.graph.vertices:
           axis[vertex] = (random.random() * 10, random.random() * 10)
        # x = []
        # y = []
        # for vertex_id in node_indices:
        #     vertex = graph.vertices[vertex_id]
        #     x.append(int(vertex.id))
        #     y.append(vertex)
         # graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=axis)
        plot.renderers.append(graph_renderer)
        output_file('graph.html')
        show(plot)
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
bg = BokehGraph(graph)
bg.draw()