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
    def __init__(self,graphStorage):
        self.graphStorage = graphStorage
    def show (self):

        node_indices =results = list(map(int,  self.graphStorage.keys()))

        plot = figure(title="Graph Layout Demonstration", x_range=(-1.1,1.1), y_range=(-1.1,1.1),tools="", toolbar_location=None)
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')

        x= []
        y= []
        for key in self.graphStorage:
            for num in self.graphStorage[key]:
                x.append(key)
                y.append(num)
        graph.edge_renderer.data_source.data = dict(start=x,end=y)

        circ = [i*2*math.pi/8 for i in node_indices]
        xcir = [math.cos(i) for i in circ]
        ycir = [math.sin(i) for i in circ]
        print(xcir, ycir)
        graph_layout = dict(zip(node_indices, zip(xcir, ycir)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)
        output_file('graph.html')
        show(plot)

test = BokehGraph(graphStorage={
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
})