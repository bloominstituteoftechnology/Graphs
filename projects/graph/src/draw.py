"""
General drawing methods for graphs using Bokeh.
"""
from random import choice, random, sample
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource, LinearColorMapper)
from bokeh.palettes import Spectral6
from graph import Graph

class BokehGraph:
    def __init__(self, graph, cc=None, connected=True):
        self.graph = graph
        self.cc = graph.find_connected()
        self.connected = connected

    def show(self):
        cc = self.cc

        # instantiate graph
        graph = self.graph
        N = len(graph.vertices)
        n = len(cc)
        node_indices = list(self.graph.vertices.keys())
        plot = figure(title='graph_demo', x_range = (-1, 10), y_range = (-1, 10), tools="", toolbar_location=None)

        graph_renderer = GraphRenderer()
        graph_renderer.node_renderer.data_source.add(node_indices, 'index')

        # randomize colors
        # if self.connected == True:
        #     colors = []
        #     graph_renderer.node_renderer.data_source.add(sorted(node_indices), 'index')
        #     for x in range(n):
        #         color = '#'+''.join([choice('0123456789ABCDEF') for i in range(6)])
        #         colors.append(color)
        # else:
        #     colors = []
        #     graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        #     for x in range(N):
        #         color = '#'+''.join([choice('0123456789ABCDEF') for i in range(6)])
        #         colors.append(color)

        colors = []
        for vertex in graph.vertices:
            colors.append(graph.vertices[vertex].color)

        print(colors)

        graph_renderer.node_renderer.data_source.add(colors,'colors')
        mapper = LinearColorMapper(palette=Spectral6, low=0, high=10)
        graph_renderer.node_renderer.glyph = Circle(radius=0.25, fill_color='colors')

        # edges
        edge_start = []
        edge_end = []
        for vertex_id in graph.vertices:
            for edge in graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(edge)
        
        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)

        # vertices
        x = []
        y = []
        for vertex_id in node_indices:
            vertex = graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        # add labels to each node/vertex
        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[vertex_id for vertex_id in graph.vertices]))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', text_color='white',text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')
        plot.add_layout(labels)
        # plot
        output_file('graph.html')
        show(plot)
