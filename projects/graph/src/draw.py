
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph, Vertex, Edge


class BokehGraph:
    def __init__(self, graph):
        self.graph = graph

    def draw(self):
        graph = self.graph
        N = len(graph.vertices)
        node_indices = list(graph.vertices.keys())

        plot = figure(title='Graph Layout Demonstration', x_range=(-7,7), y_range=(-7,7),
                      tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()
        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add(['red'] * N, 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.3, fill_color='color')

        edge_start = []
        edge_end = []

        for vert_id in node_indices:
            for v in graph.vertices[vert_id].edges:
                edge_start.append(vert_id)
                edge_end.append(v.destination)

        graph_renderer.edge_renderer.data_source.data = dict(
            start = edge_start,
            end = edge_end
        )

        x = []
        y = []

        for vert_id in node_indices:
            vertex = graph.vertices[vert_id]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        source = ColumnDataSource(data=dict(labels = node_indices,x=x, y=y))

        labels = LabelSet(x='x', y='y', text='labels', level='glyph', x_offset=5, y_offset=5, source=source, render_mode='css')
        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)
