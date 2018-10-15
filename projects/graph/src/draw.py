"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self):
        pass

    def tellme(self):
        print("sometihng")
        output_file("lines.html")
        x = [1, 2, 3, 4, 5]
        y = [6, 7, 2, 4, 5]
        p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
        p.line(x, y, legend="Temp.", line_width=2)
        show(p)


bok = BokehGraph()
bok.tellme()


