from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.palettes import Spectral8
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)

class BokehGraph:
    def __init__(self, graph):
        self.graph = graph

    def show(self):
        graph = GraphRenderer()
        node_indices = list(self.graph.vertices.keys())
        n = len(node_indices)
        plot = figure(x_range=(0, 10), y_range=(0, 10))

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color')

        graph.edge_renderer.data_source.data = dict(start=[0] * n, end=node_indices)

        x = [i for i in range(n)]
        y = [j for j in range(n)]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)
