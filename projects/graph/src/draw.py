"""
General drawing methods for graphs using Bokeh.
"""
from random import choice, random, randint
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle,
                          LabelSet, ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=30, height=30,
            show_axis=True, show_grid=True, circle_size=25,
            draw_components=True):
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
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
        self.vertex_keys = list(self.graph.vertices.keys())

        # Add the vertex data as instructions for drawing nodes
        graph_renderer.node_renderer.data_source.add(list(map(
            lambda v: v.label, self.vertex_keys)), 'index')
        colors = (self._get_connected_component_colors() if draw_components
                  else self._get_random_colors())
        graph_renderer.node_renderer.data_source.add(colors, 'color')
        # And circles
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')

        # Add the edge [start, end] indices as instructions for drawing edges
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()  # Randomize vertex coordinates, and set as layout
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        # Attach the prepared renderer to the plot so it can be shown
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self, num_colors=None):
        colors = []
        num_colors = num_colors or len(self.graph.vertices)
        for _ in range(num_colors):
            color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
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
        label_data = {'x': [], 'y': [], 'names': []}
        for vertex, position in self.pos.items():
            label_data['x'].append(position[0])
            label_data['y'].append(position[1])
            label_data['names'].append(str(vertex))
        label_source = ColumnDataSource(label_data)
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                            text_align='center', text_baseline='middle',
                            source=label_source, render_mode='canvas')
        self.plot.add_layout(labels)

    def show(self, output_path='./graph.html'):
        button = Button(label="Scramble", button_type="success")
        show(widgetbox(button))
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""
        # x = list(self.graph.vertices.keys()) / 4
        # q1 = (1, 1, self.width / 2, self.height / 2)
        # q2 = (self.width / 2, self.height / 2, self.width, 1)
        # q3 = (self.width / 2, self.height / 2, self.width, self.height)
        # q4 = (1, self.height / 2, self.width / 2, self.height)

        def _q1_put():
            return (random() * randint(2, self.width / 2 - 1),
                    random() * randint(2, self.height / 2 - 1))

        def _q2_put():
            return (random() * randint(self.width / 2 - 1, self.width - 2),
                    random() * randint(2, self.height / 2 - 1))

        def _q3_put():
            return (random() * randint(self.width / 2 - 1, self.width - 2),
                    random() * randint(self.height / 2 - 1, self.height - 2))

        def _q4_put():
            return (random() * randint(2, self.width / 2 - 2),
                    random() * randint(self.height / 2 - 1, self.height - 2))

        for index, vertex in enumerate(self.vertex_keys):
            if index < len(self.vertex_keys) / 4:
                self.pos[vertex.label] = _q1_put()
            elif index < len(self.vertex_keys) / 2:
                self.pos[vertex.label] = _q2_put()
            elif index < len(self.vertex_keys) and index < len(self.vertex_keys) * 0.75:
                self.pos[vertex.label] = _q3_put()
            else:
                self.pos[vertex.label] = _q4_put()

    def _get_connected_component_colors(self):
        """Return same-colors for vertices in connected components."""
        self.graph.find_components()
        component_colors = self._get_random_colors(self.graph.components)
        vertex_colors = []
        for vertex in self.vertex_keys:
            vertex_colors.append(component_colors[vertex.component])
        return vertex_colors
