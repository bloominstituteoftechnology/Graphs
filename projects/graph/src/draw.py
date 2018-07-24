"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8


import math
import random
from functools import reduce
from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, screenSize):
        pass  # TODO



test = Graph()  # Instantiate your graph

test.add_vertex(0)
test.add_vertex(1)
test.add_vertex(2)
test.add_vertex(3)
test.add_vertex(4)
test.add_vertex(5)
test.add_vertex(6)
test.add_vertex(7)

test.add_edge(0, 1)
test.add_edge(0, 3)
test.add_edge(1, 2)
test.add_edge(1, 3)
test.add_edge(7, 1)
test.add_edge(5, 2)
test.add_edge(7, 3)
test.add_edge(4, 3)
test.add_edge(6, 2)
test.add_edge(1, 6)

node_indices = [*test.vertices.keys()]

plot = figure(title="Graph Layout Demonstration", x_range=(0, 10), y_range=(0,10),
              tools="", toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.glyph = Circle(radius=0.2, fill_color="fill_color")
graph.node_renderer.data_source.data = dict(
    index=node_indices,
    fill_color=Spectral8)

graph.edge_renderer.data_source.data = dict(
  start=reduce(lambda x,y: x+y,[[i]*len(test.vertices[i]) for i in node_indices]),
  end=reduce(lambda x,y: x+y,[list(test.vertices[i]) for i in node_indices]))

## start of layout code
x = [random.randrange(1,9) for _ in node_indices]
y = [random.randrange(1,9) for _ in node_indices]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)