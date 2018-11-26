"""
General drawing methods for graphs using Bokeh.
"""

# necessary imports

from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (
    GraphRenderer,
    StaticLayoutProvider,
    Circle,
    LabelSet,
    ColumnDataSource,
    VeeHead,
    Arrow,
)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    # initial Bokeh graph parameters
    def __init__(
        self,
        graph,
        title="Sample Graph for Lambda Project",
        # axis width and height
        width=20,
        height=20,
        # options to display axis and/or grid
        show_axis=True,
        show_grid=False,
        # vertex/node size
        circle_size=25,
    ):
    # check if graph has vertices
        if not graph.vertices:
            raise Exception("Graph should contain vertices!")
        self.graph = graph

        # Setup plot
        self.width = width
        self.height = height
        self.pos = {}  # dict to map vertices by x, y positions
        # new plot with title and ranges
        """The bokeh.plotting interface provides a Figure class to help with assembling all the necessary objects.
            the figure() function creates Figure objects."""
        self.plot = figure(
            title=title,
            # Ranges describe the data-space bounds of a plot, in this case, from 0 to the graphs width and height
            x_range=(0, width),
            y_range=(0, height))
        # show axis and/or grid if specified
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        # call function that renders graph with passed in value for vertices size
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        # define function to render graph
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), "index"
        )
        # adds color randomizer
        graph_renderer.node_renderer.data_source.add(self._get_random_colors(), "color")
        # gives each node the shape of a circle with it's specified size and random color
        graph_renderer.node_renderer.glyph = Circle(
            size=circle_size, fill_color="color"
        )
        # adds function to get edge indexes
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        # randomize each new graph
        self.randomize()

        for i in range(len(graph_renderer.edge_renderer.data_source.data["start"])):
            # add arrows from starting node to end node
            self.plot.add_layout(
                Arrow(
                    # Arrow head size and color
                    end=VeeHead(size=20, fill_color="black"),
                    # arrow start at x, y pos of vertex
                    x_start=self.pos[
                        graph_renderer.edge_renderer.data_source.data["start"][i]
                    ][0],
                    y_start=self.pos[
                        graph_renderer.edge_renderer.data_source.data["start"][i]
                    ][1],
                    x_end=self.pos[
                        graph_renderer.edge_renderer.data_source.data["end"][i]
                    ][0],
                    y_end=self.pos[
                        graph_renderer.edge_renderer.data_source.data["end"][i]
                    ][1],
                )
            )

        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)
        self._get_labels()

    def _get_random_colors(self):
        # function to randomize colors
        colors = []
        # iterate through list of graph vertices
        for _ in range(len(self.graph.vertices)):
            # find a random color value
            color = "#" + "".join([choice("0123456789ABCDEF") for j in range(6)])
            # add to color list
            colors.append(color)
        return colors

    def _get_edge_indexes(self):
        # function to add edge between indices
        start_indices = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    # starting vertex
                    start_indices.append(vertex)
                    # ending vertex
                    end_indices.append(destination)
                # add starting vertexs to checked
                checked.add(vertex)
        # return dict of all checked edges and their indices
        return dict(start=start_indices, end=end_indices)

    # Ask Bokeh to show() or save() the results.
    # These functions save the plot to an HTML file and optionally display it in a browser.

    def show(self, output_path="./graph.html"):
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.graph.vertices:
            # TODO make bounds and random draws less hacky
            self.pos[vertex] = (
                1 + random() * (self.width - 2),
                1 + random() * (self.height - 2),
            )
            # random stuff for making vertex
            # make if statement to take into account positions already in self.pos

    def _get_labels(self):
        label_data = {"x": [], "y": [], "name": []}
        for vertex, edges in self.pos.items():
            label_data["x"].append(edges[0])
            label_data["y"].append(edges[1])
            label_data["name"].append(vertex)
        print("label", label_data)
        label_source = ColumnDataSource(label_data)
        print("label source:", label_source)

        labels = LabelSet(
            x="x",
            y="y",
            text="name",
            text_color="white",
            level="glyph",
            text_align="center",
            text_baseline="middle",
            text_line_height=1,
            source=label_source,
            render_mode="canvas",
        )
        self.plot.add_layout(labels)