"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (
    GraphRenderer,
    StaticLayoutProvider,
    Circle,
    LabelSet,
    ColumnDataSource,
)

## get bokeh up and running...
class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self):
        pass  # TODO
