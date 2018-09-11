"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=100, height=100, show_axis=False, show_grid=False, circle_size=35, draw_components=False):
        if not graph.vertices:
            raise Exception('Error: Graph has no vertices!')
        self.graph = graph
        self.width = width
        self.height = height
        self.pos = {}

        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size, draw_components)
        self._setup_labels()


    def _setup_graph_renderer(self, circle_size, draw_components):
        graph_renderer = GraphRenderer()
        self.vertex_list = list(self.graph.vertices.keys())

        graph_renderer.node_renderer.data_source.add(
            [vertex.label for vertex in self.vertex_list], 'index')
        colors = (self._get_connected_component_colors() if draw_components
            else self._get_random_colors())
        graph_renderer.node_renderer.data_source.add(colors, 'color')

        graph_renderer.node_renderer.glyph = Circle(size=circle_size, fill_color='color')

        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout = self.pos)
        self.plot.renderers.append(graph_renderer)

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
