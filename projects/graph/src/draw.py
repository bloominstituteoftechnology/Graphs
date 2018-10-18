"""
General drawing methods for graphs using Bokeh.
"""
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (
    GraphRenderer,
    StaticLayoutProvider,
    Oval,
    LabelSet,
    ColumnDataSource,
)

# from bokeh.palettes import Spectral4
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        self.graph = graph
        self.keys = []
        self.values = []
        """
        {
            '0': {'1', '3'},
            '1': {'0'},
            '2': set(),
            '3': {'0'}
        }
        """
        for key in self.graph.vertices:
            for edge in self.graph.vertices[key]:
                self.keys.append(key)
                self.values.append(edge)

        print("keys:", self.keys)
        print("values:", self.values)

    def draw(self):
        # N = 4

        node_indices = list(self.graph.vertices.keys())
        print("Node indicies", node_indices)

        plot = figure(
            title="Graph Layout Demonstration",
            x_range=(-1.1, 1.1),
            y_range=(-1.1, 1.1),
            tools="",
            toolbar_location=None,
        )

        graph = GraphRenderer()
        # print("GraphRenderer() ", graph)

        g = graph.node_renderer.data_source.add(node_indices, "index")
        # print("NODE_INDICES: ", g)
        # c = graph.node_renderer.data_source.add(Spectral4, "color")
        # print("COLORS: ", c)
        graph.node_renderer.glyph = Oval(height=0.1, width=0.1, fill_color="pink")

        # start is a list that has N elements. Each element is '0'.
        # start=[0, 0, 1, 3] end=[1, 3, 0, 0]
        d = graph.edge_renderer.data_source.data = dict(
            start=self.keys, end=self.values
        )
        # print("DICT: ", d)

        ### start of layout code
        circ = [int(i) * 2 * math.pi / 4 for i in node_indices]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]
        # print("CIRC, X, Y", circ, x, y)

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file("graph.html")
        show(plot)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex("0")
# graph.add_vertex("1")
# graph.add_vertex("2")
# graph.add_vertex("3")
# graph.add_edge("0", "1")
# graph.add_edge("0", "3")

# bg = BokehGraph(graph)  # this should only create the object instance
# bg.draw()  # should actually generate the graph
