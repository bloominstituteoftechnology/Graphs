"""
General drawing methods for graphs using Bokeh.
"""

from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, Arrow, NormalHead


def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(
        self,
        graph,
        title="Graph",
        width=10,
        height=10,
        show_axis=False,
        show_grid=False,
        circle_size=35,
    ):
        if not graph.vertices:
            raise Exception("Graph should contain vertices!")
        self.graph = graph

        # Setup plot
        self.edge_coords = []
        self.width = width
        self.height = height
        self.pos = {}  # dict to map vertices to x, y positions
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), "index"
        )
        graph_renderer.node_renderer.data_source.add(self._get_random_colors(), "color")
        graph_renderer.node_renderer.glyph = Circle(
            size=circle_size, fill_color="color"
        )

        self.generate()

        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self):
        colors = []
        for _ in range(len(self.graph.vertices)):
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
                    start_indices.append(vertex)
                    end_indices.append(destination)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def show(self, output_path="./graph.html"):
        output_file(output_path)
        show(self.plot)

    def place_vert(self, vertex):
        acceptable = False

        while not acceptable:
            random_x = 1 + random() * (self.width - 2)
            random_y = 1 + random() * (self.height - 2)
            acceptable = True
            for i in self.pos:
                if (
                    (random_x - self.pos[i][0]) ** 2 + (random_y - self.pos[i][1]) ** 2
                ) ** .5 < 1:
                    acceptable = False
                    print("Rejected position, rerolling...")
            for edge_coord in self.edge_coords:
                x_start, x_end, y_start, y_end = edge_coord
                x_vert = random_x
                y_vert = random_y
                if (
                    abs(
                        (y_end - y_start) * x_vert
                        - (x_end - x_start) * y_vert
                        + x_end * y_start
                        - y_end * x_start
                    )
                    / (((y_end - y_start) ** 2 + (x_end - x_start) ** 2) ** (1 / 2))
                    < .6
                ):
                    acceptable = False
                    print("Rejected position due to line conflict")

        self.pos[vertex] = (random_x, random_y)

    def place_edge(self, start, end):

        print(self.edge_coords)
        if start > end:
            coefficient = 1
        else:
            coefficient = -1

        start_new = False
        end_new = False

        if start not in self.pos:
            self.place_vert(start)
            start_new = True

        if end not in self.pos:
            self.place_vert(end)
            end_new = True

        acceptable = False

        while not acceptable:
            x_start = self.pos[start][0]
            y_start = self.pos[start][1]
            x_end = self.pos[end][0]
            y_end = self.pos[end][1]
            acceptable = True
            for i in self.pos:
                if i != start and i != end:
                    x_vert = self.pos[i][0]
                    y_vert = self.pos[i][1]
                    if (
                        abs(
                            (y_end - y_start) * x_vert
                            - (x_end - x_start) * y_vert
                            + x_end * y_start
                            - y_end * x_start
                        )
                        / (((y_end - y_start) ** 2 + (x_end - x_start) ** 2) ** (1 / 2))
                        < .6
                    ):
                        print("AAAAAAHHH!")
                        if start_new:
                            self.place_vert(start)
                            acceptable = False
                        elif end_new:
                            self.place_vert(end)
                            acceptable = False

            for edge_coord in self.edge_coords:
                if intersect(
                    (x_start, y_start),
                    (x_end, y_end),
                    (edge_coord[0], edge_coord[2]),
                    (edge_coord[1], edge_coord[3]),
                ):
                    if start_new:
                        self.place_vert(start)
                        acceptable = False
                    elif end_new:
                        self.place_vert(end)
                        acceptable = False

        self.edge_coords.append([x_start, x_end, y_start, y_end])

        self.plot.add_layout(
            Arrow(
                end=NormalHead(fill_color="orange", size=10),
                x_start=x_start,
                y_start=y_start,
                x_end=x_end,
                y_end=y_end,
            )
        )

    def generate(self):
        """Randomize vertex positions."""
        edges = self._get_edge_indexes()

        for i in range(len(edges["start"])):

            self.place_edge(edges["start"][i], edges["end"][i])

        for vertex in self.graph.vertices:
            if vertex not in self.pos:
                self.place_vert(vertex)
