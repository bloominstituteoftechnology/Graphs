"""
General drawing methods for graphs using Bokeh.
"""
import math
from graph import Graph
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Oval, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8

# N = 8
# node_indices = list(range(N))

# plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
#               tools='', toolbar_location=None)

# graph = GraphRenderer()

# #makes the actual node
# graph.node_renderer.data_source.add(node_indices, 'index')
# #duno what this does but its blank without it
# # graph.node_renderer.data_source.add(Spectral8, 'color')
# #makes the lil colored circles
# graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='red')

# #makes the edges
# graph.edge_renderer.data_source.data = dict(
#     start=[0, 0, 0, 0, 0, 0, 0, 0, 1],
#     end=[0, 1, 2, 3, 4, 5, 6, 7, 5])

# ## start of layout code
# circ = [i*2*math.pi/8 for i in node_indices]
# x = [math.cos(i) for i in circ]
# y = [math.sin(i) for i in circ]

# graph_layout = dict(zip(node_indices, zip(x, y)))
# graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# plot.renderers.append(graph)

# output_file('graph.html')
# show(plot)



class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, lilgraph):
        self.lilgraph = lilgraph
        self.keys = []
        self.values = [] 
        for key in self.lilgraph.vertices:
            for value in self.lilgraph.vertices[key].edges:
                self.keys.append(key)
                self.values.append(value)
        vertices = list(lilgraph.vertices.keys())
        plot = figure(title='One heckin graph', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools='', toolbar_location=None)
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(vertices, 'index')
        graph.node_renderer.glyph = Oval(height=0.05, width=0.05, fill_color='pink')
        graph.edge_renderer.data_source.data = dict(
            start=self.keys,
            end=self.values)
        circ = [i*2*math.pi/8 for i in vertices]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]
        graph_layout = dict(zip(vertices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
        plot.renderers.append(graph)
        show(plot)
        output_file('graph.html')

test = Graph()
test.add_vertex(1)
test.vertices[1].add_edge(2)
test.vertices[1].add_edge(3)
test.add_vertex(2)
test.add_vertex(3)
test.add_vertex(4)

draw = BokehGraph(test)

    
