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
# declare constants
WIDTH = (10,)
HEIGHT = (10,)
ALLOW_AXIS = (False,)
ALLOW_GRID = (False,)
VERT_SIZE = (20,)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(
        self,
        graph,
        width,
        height,
        allow_grid,
        allow_axis,
        vert_size,
        color,
        title="My Graph",
    ):
        if graph.vertices:
            raise Exception("No verts have been defined!")
        self.graph = graph

        self.render_graph(vert_size)
        self.width = WIDTH
        self.height = HEIGHT
        self.plot.grid.visible = ALLOW_GRID
        self.plot.axis.visible = ALLOW_AXIS
        self.plot = figure(x_range(0, width), y_range(0, height), title=title)
        self.pos = {}

    def render_graph(self, vert_size):
        display_graph = GraphRenderer(kwargs)

        display_graph.node__renderer.data_src.data = self.get_edges()
        pass  # TODO

    def get_edges(self):
        pass  # TODO


## exercise
# connected_components = []
# visited = set()

# for v in graph.verts:
#     if v not in visited:
#         visited.add(v)
#         components = bfs(v)
#         connected_components.push(components)
