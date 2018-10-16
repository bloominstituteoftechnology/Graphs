import math
from graph import Graph

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, LabelSet, ColumnDataSource
from bokeh.palettes import Spectral8


class BokehGraph:
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graphDraw = self.graph
        N = len(graphDraw.graph)
        node_indices = list(graphDraw.graph.keys())

        plot = figure(title='Graph Layout Demonstration', x_range=(-7,7), y_range=(-7,7),
                    tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        # graph_renderer.node_renderer.data_source.add(Spectral8, 'color')
        graph_renderer.node_renderer.glyph = Oval(height=1, width=1, fill_color='yellow')

        edge_start = []
        edge_end = []

        for vertex in node_indices:
            for v in graphDraw.graph[vertex].edges:
                edge_start.append(vertex)
                edge_end.append(v)
        print('start', edge_start)
        print('end', edge_end)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end
            )
        print(graph_renderer.edge_renderer.data_source.data)

        x = []
        y = []
        ### start of layout code
        for vertex_id in node_indices:
            vertex = graphDraw.graph[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        source = ColumnDataSource(
            data=dict(
                x = x,
                y = y,
                names = node_indices
            )
        )

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


graph = Graph()  
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')


bg = BokehGraph(graph)
bg.draw()
