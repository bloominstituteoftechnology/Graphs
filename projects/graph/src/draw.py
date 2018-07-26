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
from bokeh.models import Arrow, NormalHead

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
        # color,
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

        display_graph.node_renderer.data_src.add(
            list(self.graph.vertices.keys()), "index"
        )
        display_graph.node_renderer.data_src.add(self.get_colors(), "color")
        display_graph.node_renderer.glyph = Circle(size=vert_size, fill_color="color")

        display_graph.node__renderer.data_src.data = self.get_edges()
        self.randomize()
        for i in range(len(display_graph.edge_renderer.data_src.data["start"])):
            self.plot.add_layout(
                Arrow(
                    end=NormalHead(fill_color="blue"),
                    x_start=self.pos[
                        display_graph.edge_renderer.ddata.src.data["start"][i]
                    ][0],
                    x_end=self.pos[
                        display_graph.edge_renderer.ddata.src.data["end"][i]
                    ][0],
                    y_start=self.pos[
                        display_graph.edge_renderer.ddata.src.data["start"][i]
                    ][1],
                    y_end=self.pos[
                        display_graph.edge_renderer.ddata.src.data["end"][i]
                    ][1],
                )
            )

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
