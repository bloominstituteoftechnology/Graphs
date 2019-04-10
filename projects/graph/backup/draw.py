"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph.py import Graph
from queue.py import Queue


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self):
        self.graph = Graph()

  