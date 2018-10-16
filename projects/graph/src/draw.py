"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self):
        # output to static HTML file
        output_file("graph1.html")

# create a new plot with a title and axis labels
        p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
        p.line(x, y, legend="Temp.", line_width=2)

# show the results
        show(p)
