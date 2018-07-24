"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider,
Circle, LabelSe, ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=10, height=10,
                show_axis=False, show_grid=False, circle_size=)

    if not graph.vertices:
            raise Expception('graph should contain vertices!')
    self.graph = graph

    #Setup plot 
                   
        pass  # TODO
