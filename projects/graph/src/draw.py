"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.Graph = graph #should be a object. instance of Graph
        

    
test = Graph()
test.add_vertex("0")
test.add_vertex("1")
test.add_vertex("2")
test.add_edge("0", "2")
test.add_edge("1", "2")
test.add_edge("0", "2")
