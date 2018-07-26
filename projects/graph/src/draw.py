"""
General drawing methods for graphs using Bokeh.
"""
import math
from random import sample
from bokeh.io import show, output_file
from bokeh.palettes import Category10
from bokeh.plotting import figure
from bokeh.models import (
    GraphRenderer,
    StaticLayoutProvider,
    Circle
)
from graph import Graph


class BokehGraph:
    """
    Class that takes a graph and exposes drawing methods.
    """
    def __init__(self, graph, title='Graph', width=1000, height=800,
                 vertex_size=20, grid_visible=False, axis_visible=False):
        self.graph = graph
        self.title = title
        self.height = height
        self.width = width
        self.vertex_size = vertex_size
        self.plot = figure(title=title, plot_width=width, plot_height=height,
                           x_range=(0, width), y_range=(0, height),
                           toolbar_location=None)
        self.plot.axis.visible = axis_visible
        self.plot.grid.visible = grid_visible
        self._render_graph()

    def _render_graph(self):
        """
        Sets up renderers for vertices(nodes) and edges
        """
        graph_renderer = GraphRenderer()
        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        graph_renderer.node_renderer.data_source.add(Category10[10], 'color')
        graph_renderer.node_renderer.glyph = Circle(size=self.vertex_size,
                                                    fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edges()
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self._get_random_node_positions())
        self.plot.renderers.append(graph_renderer)

    def _get_edges(self):
        """
        Returns start and end vertices for each edge in a dictionary
        """
        start = []
        end = []
        for vertex, edges in self.graph.vertices.items():
            for edge in edges:
                start.append(vertex)
                end.append(edge.label)
        return {'start': start, 'end': end}

    def _get_random_node_positions(self):
        """
        Assigns a random x, y position to each vertex and returns coordinates
        in a dictionary
        """
        start = self.vertex_size
        x_range = list(range(start, int(self.width - start), start))
        y_range = list(range(start, int(self.height - start), start))
        x = sample(x_range, len(self.graph.vertices))
        y = sample(y_range, len(self.graph.vertices))
        return dict(zip(self.graph.vertices.keys(), zip(x, y)))

    def show(self, output_path='./graph.html'):
        """
        Saves Bokeh graph plot to an HTML file and displays in browser
        """
        output_file(output_path)
        show(self.plot)


# Temp test code
graph = Graph()
graph.add_vertex('V1')
graph.add_vertex('V2')
graph.add_vertex('V3')
graph.add_vertex('V4')
graph.add_vertex('V5', ['V3'])
graph.add_vertex('V6')
graph.add_vertex('V7', ['V6', 'V1'])
graph.add_edge('V1', 'V2', False)
graph.add_edge('V2', 'V4', False)
graph.add_edge('V2', 'V3', False)
graph.add_edge('V3', 'V5')
graph.add_edge('V4', 'V7', False)
graph.add_edge('V4', 'V6', False)
bg = BokehGraph(graph)
bg.show()
