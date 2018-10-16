"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, Oval, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self):
        pass  # TODO




graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '2')
graph.add_edge('0', '3')
print(graph.vertices)

print(graph.dfs('0'))
