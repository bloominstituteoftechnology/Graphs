# """
# General drawing methods for graphs using Bokeh.
# """

# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
#                           ColumnDataSource)


# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#     def __init__(self):
#         pass  # TODO

import math
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, Oval
from bokeh.palettes import Spectral8

N = 8
node_indices = list(range(N))

plot = figure(title="Graph Layout Demonstration", x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools="", toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color="fill_color")
graph.node_renderer.data_source.data = dict(
    index=node_indices,
    fill_color=Spectral8)

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)
