"""
General drawing methods for graphs using Bokeh.
"""
import math

from graph import Graph
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8
#from bokeh.io import show, output_file
#from bokeh.plotting import figure
#from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
#                          ColumnDataSource)

#
class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
        self.start_verts = []
        self.end_verts = []

    def generate_edges(self):
        """
        {
            '0', {'1', '3'},
            '1', {'0'}
        }
        """
        for key in self.graph.vertices:
            for edge in self.graph.vertices[key].edges:
                self.start_verts.append(key)
                self.end_verts.append(edge)

        print('self.start_verts:', self.start_verts)
        print('self.end_verts:', self.end_verts)

    def draw(self):
        # N = 8
        self.generate_edges()
        node_indices = list(self.graph.vertices.keys())

        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
                    tools='', toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        # graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='pink')

        # start = [0, 0, 1, 3]
        # end = [1, 3, 0, 0]
        graph.edge_renderer.data_source.data = dict(
            start=self.start_verts,
            end=self.end_verts)

        ### start of layout code
        circ = [int(i)*2*math.pi/8 for i in node_indices]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot) 

graph = Graph()
# TODO: Add vertices and edges here
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
bokeh = BokehGraph(graph)
bokeh.draw()

