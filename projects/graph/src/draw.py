"""
General drawing methods for graphs using Bokeh.
"""
from random import sample
from bokeh.io import show, output_file
from bokeh.palettes import Category10
from bokeh.plotting import figure
from bokeh.models import (
    GraphRenderer,
    StaticLayoutProvider,
    Circle
)


class BokehGraph:
    """
    Class that takes a graph and exposes drawing methods.
    """
    def __init__(self, graph, show_components, title='Graph', 
                 file_name='./graph.html', width=1000, height=800,
                 vertex_size=20, grid_visible=False, axis_visible=False):
        self.graph = graph
        self.title = title
        self.file_name = file_name
        self.height = height
        self.width = width
        self.vertex_size = vertex_size
        self.show_components = show_components
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
        graph_renderer.node_renderer.data_source.add(
            self._get_colors(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=self.vertex_size,
                                                    fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edges()
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self._get_random_node_positions())
        self.plot.renderers.append(graph_renderer)

    def _get_colors(self):
        if self.show_components:
            colors = []
            for vertex in self.graph.vertices.keys():
                component = self.graph.vertex_obj_map[vertex].component
                colors.append(Category10[10][component])
            return colors
        return Category10[10]

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

    def show(self):
        """
        Saves Bokeh graph plot to an HTML file and displays in browser
        """
        output_file(self.file_name)
        show(self.plot)
