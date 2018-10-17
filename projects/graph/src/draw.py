"""
General drawing methods for graphs using Bokeh.
"""
from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=10, height=10,
                show_axis=False, show_grid=False, circle_size=35):
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
        self.graph = graph

        #setup plot
        self.width = width
        self.height = height
        self.pos = {}
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    # starting with underscore means that it's internal, warning, no need to change things here for UX.
    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        graph.renderer.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')
        graph_render.edge_end.data_source.data = self._get_edge_indexes()
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self):
        colors = []
        for _ in range(len(self.graph_vertices)):
            color = "#"+''.join([voice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors

    def _get_edge_indexes(self):
        start_indicies = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.apend(vertex)
                    end_indices.append(destination)
                checked.add(vertex)

        return dict(start=start_indicies, end=end_indices)

    def show(self, output_path='./draw.html'):
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.graph.vertices:
            self.pos[vertex] = (1 + random() * (self.width - 2),
                                1 + random() * (self.height - 2))
        


# graph = {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }

# p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# p.line(x, y, legend="Temp.", line_width=2)


# import math

# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
# from bokeh.palettes import Spectral8
# from graph import Graph


# N = len(graph.vertices)
# node_indices = list(graph.vertices)

# plot = figure(
#     title="Graph Layout Demonstration",
#     x_range=(-1.1, 10.1),
#     y_range=(-1.1, 10.1),
#     tools="",
#     toolbar_location=None,
# )

# graph_renderer = GraphRenderer()

# graph_renderer.node_renderer.data_source.add(node_indices, "index")
# graph_renderer.node_renderer.data_source.add(Spectral8, "color")
# graph_renderer.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color="color")

# start_indices = []
# end_indices = []

# for vertex in graph.vertices:
#     for edge in graph.vertices[vertex]:
#         start_indices.append(vertex)
#         end_indices.append(edge_end)

# graph_renderer.edge_renderer.data_source.data = dict(
#     start=start_indices, 
#     end=end_indices)

# ### start of layout code
# circ = [int(v) for v in graph.vertices]
# print("circ ", circ)
# x = [2 * (i // 3) for i in circ]
# y = [2 * (i % 3) for i in circ]

# graph_layout = dict(zip(node_indices, zip(x, y)))
# graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# plot.renderers.append(graph_renderer)

# output_file("graph.html")
# show(plot)
