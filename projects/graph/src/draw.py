"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)

graph = {
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

p.line(x, y, legend="Temp.", line_width=2)

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self):
        pass  # TODO
