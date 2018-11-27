import math
from graph import Graph

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource, CategoricalColorMapper
from bokeh.palettes import Spectral8


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

        edge_start = []
        edge_end = []

        for vertex in node_indices:
            for edge in graph.vertices[vertex].edges:
                edge_start.append(vertex)
                edge_end.append(edge)

        print('edge start', edge_start)
        print('edge end', edge_end)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end
            )

 
        x = []
        y = []
        ### start of layout code
        for vertex_id in node_indices:
            vertex = graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        source = ColumnDataSource(
            data=dict(
                x = x,
                y = y,
                names = node_indices
            )
        )


        color_mapper = [''] * len(node_indices)

        for index, node in enumerate(node_indices):
            print('color mapper', color_mapper)
            for edge in edge_start:
                if node == edge:
                    print('equals')
                    color_mapper[index] = 'red'

        for index, color in enumerate(color_mapper):
            if color == '':
                color_mapper[index] = 'blue'


        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add(color_mapper, 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=.40, fill_color='color')
        
        graph_renderer_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_renderer_layout)

        labels= LabelSet(
            x = 'x', 
            y = 'y', 
            text='names', 
            level='glyph',
            x_offset = -4,
            y_offset = -8,
            source = source,
            render_mode = 'canvas' 
        )

        plot.renderers.append(graph_renderer)
        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)



