"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle,
                          LabelSet, ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self,
                 graph,
                 title='Graph',
                 width=10,
                 height=10,
                 show_axis=False,
                 show_grid: False,
                 circle_size=35):
        if not graph.vertices:
            raise Exception('Graph should contain vertices')
        self.graph = graph

        # Setup plot
        self.width = width
        self.height = height
        self.pos = {}  # dict to map vertices to x, y positions
        self.plot = figure(title=title, x_range=(0, width), y_range(0, height))

        self.plot.axis.visible = show_axis
        self.plot.axis.visible = show_grid

    def _setup_graph_renderer(self, circle):
        pass

    def show(self):
        pass
