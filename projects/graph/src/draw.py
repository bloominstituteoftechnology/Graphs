"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graphStorage):
        self.graphStorage = graphStorage

    def show(self):

        node_indices = list(map(int,  self.graphStorage.keys()))

        plot = figure(title="Graph Layout Demonstration", x_range=(-1.1, 1.1),
                      y_range=(-1.1, 1.1), tools="", toolbar_location=None)
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.glyph = Circle(radius=.05, fill_color='black')
        x = []
        y = []
        for key in self.graphStorage:
            for num in self.graphStorage[key]:
                x.append(key)
                y.append(num)
        graph.edge_renderer.data_source.data = dict(start=x, end=y)

        circ = [i*2*math.pi/len(node_indices) for i in node_indices]
        xcir = [math.cos(i) for i in circ]
        ycir = [math.sin(i) for i in circ]
        graph_layout = dict(zip(node_indices, zip(xcir, ycir)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
        source = ColumnDataSource(
            dict(xvals=xcir, yvals=ycir, name=node_indices))

        labels = LabelSet(x='xvals', y='yvals', text='name', x_offset=-4,
                          y_offset=-8, level='glyph', source=source, text_color='white')

        plot.renderers.append(graph)
        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)
