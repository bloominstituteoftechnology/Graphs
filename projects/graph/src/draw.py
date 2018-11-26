# """
# General drawing methods for graphs using Bokeh.
# """
# import math

# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import (
#     GraphRenderer,
#     StaticLayoutProvider,
#     Oval,
#     LabelSet,
#     ColumnDataSource,
# )

# # from bokeh.palettes import Spectral4
# from graph import Graph


# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""

#     def __init__(self, graph):
#         self.graph = graph
#         self.keys = []
#         self.values = []
#         """
#         {
#             '0': {'1', '3'},
#             '1': {'0'},
#             '2': set(),
#             '3': {'0'}
#         }
#         """
#         for key in self.graph.vertices:
#             for edge in self.graph.vertices[key]:
#                 self.keys.append(key)
#                 self.values.append(edge)

#         print("keys:", self.keys)
#         print("values:", self.values)

#     def draw(self):
#         # N = 4

#         node_indices = list(self.graph.vertices.keys())
#         print("Node indicies", node_indices)

#         plot = figure(
#             title="Graph Layout Demonstration",
#             x_range=(-1.1, 1.1),
#             y_range=(-1.1, 1.1),
#             tools="",
#             toolbar_location=None,
#         )

#         graph = GraphRenderer()
#         # print("GraphRenderer() ", graph)

#         g = graph.node_renderer.data_source.add(node_indices, "index")
#         # print("NODE_INDICES: ", g)
#         # c = graph.node_renderer.data_source.add(Spectral4, "color")
#         # print("COLORS: ", c)
#         graph.node_renderer.glyph = Oval(height=0.1, width=0.1, fill_color="pink")

#         # start is a list that has N elements. Each element is '0'.
#         # start=[0, 0, 1, 3] end=[1, 3, 0, 0]
#         d = graph.edge_renderer.data_source.data = dict(
#             start=self.keys, end=self.values
#         )
#         # print("DICT: ", d)

#         ### start of layout code
#         circ = [int(i) * 2 * math.pi / 4 for i in node_indices]
#         x = [math.cos(i) for i in circ]
#         y = [math.sin(i) for i in circ]
#         # print("CIRC, X, Y", circ, x, y)

#         graph_layout = dict(zip(node_indices, zip(x, y)))
#         graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

#         plot.renderers.append(graph)

#         output_file("graph.html")
#         show(plot)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex("0")
# graph.add_vertex("1")
# graph.add_vertex("2")
# graph.add_vertex("3")
# graph.add_edge("0", "1")
# graph.add_edge("0", "3")

# bg = BokehGraph(graph)  # this should only create the object instance
# bg.draw()  # should actually generate the graph


#################################################################
#################################################################
"""
General drawing methods for graphs using Bokeh.
"""
from math import ceil, floor, sqrt
from random import choice, random
from bokeh.io import show, output_file
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet


class BokehGraph:
    """Class that takes a graph and exposes drawing methods.""" """Class that takes a graph and exposes drawing methods."""


def __init__(
    self,
    graph,
    title="Graph",
    width=100,
    height=100,
    show_axis=False,
    show_grid=False,
    circle_size=35,
    draw_components=False,
):
    if not graph.vertices:
        raise Exception("Graph should contain vertices!")
    self.graph = graph
    self.width = width
    self.height = height
    self.pos = {}  # dict to map vertices to x, y positions
    # Set up plot, the canvas/space to draw on
    self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
    self.plot.axis.visible = show_axis
    self.plot.grid.visible = show_grid
    self._setup_graph_renderer(circle_size, draw_components)
    self._setup_labels()

    def _setup_graph_renderer(self, circle_size, draw_components):
        # The renderer will have the actual logic for drawing
        graph_renderer = GraphRenderer()
        # Saving vertices in an arbitrary but persistent order
        self.vertex_list = list(self.graph.vertices.keys())
        # Add the vertex data as instructions for drawing nodes
        graph_renderer.node_renderer.data_source.add(
            [vertex.label for vertex in self.vertex_list], "index"
        )
        colors = (
            self._get_connected_component_colors()
            if draw_components
            else self._get_random_colors()
        )
        graph_renderer.node_renderer.data_source.add(colors, "color")
        # And circles
        graph_renderer.node_renderer.glyph = Circle(
            size=circle_size, fill_color="color"
        )
        # Add the edge [start, end] indices as instructions for drawing edges
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()  # Randomize vertex coordinates, and set as layout
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        # Attach the prepared renderer to the plot so it can be shown
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self, num_colors=None):
        colors = []
        num_colors = num_colors or len(self.graph.vertices)

        for _ in range(num_colors):
            color = "#" + "".join([choice("0123456789ABCDEF") for j in range(6)])
            colors.append(color)
        return colors

        def _get_edge_indexes(self):
            start_indices = []
            end_indices = []
            checked = set()

            for vertex, edges in self.graph.vertices.items():
                if vertex not in checked:
                    for destination in edges:
                        start_indices.append(vertex.label)
                        end_indices.append(destination.label)
                    checked.add(vertex)
                return dict(start=start_indices, end=end_indices)

    def _setup_labels(self):
        label_data = {"x": [], "y": [], "names": []}

        for vertex_label, (x_pos, y_pos) in self.pos.items():
            label_data["x"].append(x_pos)
            label_data["y"].append(y_pos)
            label_data["names"].append(vertex_label)
        label_source = ColumnDataSource(label_data)
        labels = LabelSet(
            x="x",
            y="y",
            text="names",
            level="glyph",
            text_align="center",
            text_baseline="middle",
            source=label_source,
            render_mode="canvas",
        )
        self.plot.add_layout(labels)

        def show(self, output_path="./graph.html"):
            # """Render the graph to a file on disk and open with default browser."""
            output_file(output_path)
            show(self.plot)

    def randomize(self):
        # """Randomize vertex positions, trying to minimize collisions."""
        # Split space into a grid of ~sqrt(num_of_vertices)^2
        rows = floor(sqrt(len(self.vertex_list)))
        cols = ceil(sqrt(len(self.vertex_list)))
        grid_height = self.height / rows
        grid_width = self.width / cols

        for i, vertex in enumerate(self.vertex_list):
            # Randomly place each vertex in a different grid cell
            # TODO: improve, this spreads things out some but still collides
            col = (i % rows) + 1
            row = (i + 1) // cols
            x_pos = 10 + (col + random()) * grid_width - 15
            y_pos = 10 + (row + random()) * grid_height - 15
            self.pos[vertex.label] = (x_pos, y_pos)

    def _get_connected_component_colors(self):
        # """Return same-colors for vertices in connected components."""
        self.graph.find_components()
        component_colors = self._get_random_colors(self.graph.components)
        vertex_colors = []

        for vertex in self.vertex_list:
            vertex_colors.append(component_colors[vertex.component])
        return vertex_colors
