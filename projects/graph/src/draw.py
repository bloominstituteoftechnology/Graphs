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
        # Many arguments, but all but 'graph' have default values
        # pylint: disable=too-many-arguments
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')

        # Setup plot
        self.graph = graph  # assuming graph is dict of vertex_label: edges_set
        self.width = width
        self.height = height
        self.pos = {}  # dict that will map vertices to x, y positions
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        graph_renderer.node_renderer.data_source.add(self._get_random_colors(),
                                                     'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize(show_graph=False)  # Set up initial random vertex positions
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self):
        colors = []
        for _ in range(len(self.graph.vertices)):
            color = "#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
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

    def _setup_labels(self):
        label_data = {'x': [], 'y': [], 'names': []}
        for vertex, position in self.pos.items():
            label_data['x'], label_data['y'] = position
            label_data['name'] = str(vertex)
        label_source = ColumnDataSource(label_data)

        # TODO:  Label styles
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                          text_align='center', text_baseline='middle',
                          source=label_source, render_mode='canvas')
        self.plot.add_layout(labels)


    def show(self, output_path='./graph.html'):
        """Generate HTML with the Bokeh graph and open default web browser."""
        output_file(output_path)
        show(self.plot)

    def randomize(self, show_graph=True):
        """Randomize vertex position and optionally show the graph."""
        for vertex in self.graph.vertices:
            self.pos[vertex] = (1 + (random() * (self.width - 2)),
                                1 + (random() * (self.height - 2)))
        if show_graph:
            self.show()
