"""
General drawing methods for graphs using Bokeh.
"""
import random

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    def show(self):
        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1), y_range=(-1.1,10.1),
                    tools='', toolbar_location=None)
                    
        N = len(self.graph.vertices)
        node_indices = list(self.graph.vertices)

        graph = GraphRenderer()

        hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        colorString = '#'
        colors = []

        for _ in range(N):
            for _ in range(0, 3):
                colorString += hexValues[random.randint(0, len(hexValues) - 1)]

            colors.append(colorString)
            colorString = '#'

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(colors, 'color')
        graph.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex in self.graph.vertices:
            for edge in self.graph.vertices[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge)

        graph.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)

        grid = [int(v) for v in self.graph.vertices]
        x = [2 * (i // 3) + i / 10 * (i % 3) for i in grid]
        y = [2 * (i % 3)  + i / 10 * (i // 3)for i in grid]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', 
        text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')
        
        plot.renderers.append(graph)
        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)
