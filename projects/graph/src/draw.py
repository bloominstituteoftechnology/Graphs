"""
General drawing methods for graphs using Bokeh.
"""

from random import randint
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle,
                          LabelSet, ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph, height, width):
        self.graph = graph
        self.width = width
        self.height = height
        self.node_indices = list(graph.vertices.keys())
        self.plot = figure(title='Graph', x_range=(0, width),
                           y_range=(0, height), tools='',
                           toolbar_location=None)
        self.renderer = GraphRenderer()

    def make_graph(self):
        self.renderer.node_renderer.data_source.add(self.node_indices, 'index')
        self.renderer.node_renderer.glyph = Circle(size=25, fill_color='color')
        self.connect_nodes()
        self.renderer.edge_renderer.data_source.data = self.graph.get_edges()
        self.renderer.node_renderer.data_source.add(list(self.graph.get_colors()),
                                                    'color')
        # took from here - POS
        self.position_nodes()
        self.plot.renderers.append(self.renderer)
        output_file('graph.html')
        show(self.plot)

    def connect_nodes(self):
        connected = set()
        for node in self.graph.vertices:
            if self.graph.vertices[node] not in connected:
                connected_nodes = self.graph.connect(node)
                connected |= connected_nodes

    def position_nodes(self):
        data = {'x': [], 'y': [], 'names': [], 'text_color': []}
        used_pos = set()
        for node in self.graph.vertices:
            while True:
                width = randint(2, self.width - 5)
                height = randint(2, self.height - 5)
                p = (width, height)
                if p not in used_pos:
                    data['x'].append(width)
                    data['y'].append(height)
                    # used_pos.add(p)
                    padded_xs = (x for x in range(p[0] - 2, p[0] + 2))
                    padded_ys = (y for y in range(p[1] - 2, p[1] + 2))
                    # bad complexity, but trying things out
                    for w in padded_xs:
                        for h in padded_ys:
                            used_pos.add((w, h))
                    data['names'].append(self.graph.vertices[node].label)
                    data['text_color'].append('#000')
                    break

        layout = dict(
            zip(self.node_indices, list(zip(data['x'], data['y']))))
        self.renderer.layout_provider = (
            StaticLayoutProvider(graph_layout=layout))

        nodes = LabelSet(x='x',
                         y='y',
                         text='names',
                         text_color='text_color',
                         # x_offset=20,
                         # y_offset=20,
                         level='overlay',
                         text_align='center',
                         text_baseline='middle',
                         source=ColumnDataSource(data),
                         render_mode='canvas')

        self.plot.add_layout(nodes)
