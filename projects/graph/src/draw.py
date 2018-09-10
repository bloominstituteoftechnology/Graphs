"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph
from graph import graph

class BokehGraph(Graph):
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self):
        Graph.__init__(self)

    def show(self):
        output_file("graph.html")
        p = figure(title="Graphs Part 2")
        p.line(graph, line_width=2)
        show(p)

BokehGraph.show(graph)