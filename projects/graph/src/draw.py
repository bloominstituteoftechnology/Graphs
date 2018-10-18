"""
General drawing methods for graphs using Bokeh.
"""

import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)
from bokeh.palettes import Viridis256
from graph import Graph


class BokehGraph:
    def __init__(self, graph):
        self.graph = graph

    def show(self):
        graph = self.graph
        node_indices = list(self.graph.vertices)
        N = len(node_indices)
        # print(node_indices)
        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1, 15.1), y_range=(-1.1, 15.1), tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        colors = Viridis256[0:N]
        # print(colors)

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add(colors , 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=.2, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex_id in graph.vertices:
            for edge_end in graph.vertices[vertex_id].edges:
                start_indices.append(vertex_id)
                end_indices.append(edge_end)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)

         # start of layout code
        # circ = [int(v*2*math.pi/8) for v in self.graph.vertices]
        linear = [int(v*2*math.pi/8) for v in self.graph.vertices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]

        x = [graph.vertices[vertex_id].x for vertex_id in graph.vertices]
        y = [graph.vertices[vertex_id].y for vertex_id in graph.vertices]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[graph.vertices[vertex_id].value for vertex_id in graph.vertices]))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)


# graph = Graph()
# bokeh = BokehGraph(graph)
# bokeh.graph.add_vertex('0')
# bokeh.graph.add_vertex('1')
# bokeh.graph.add_vertex('2')
# bokeh.graph.add_vertex('3')
# bokeh.graph.add_edge('0', '1')
# bokeh.graph.add_edge('0', '3')
# bokeh.graph.add_edge('2', '3')
# bokeh.graph.add_vertex('4')
# bokeh.graph.add_edge('2', '4')
# bokeh.graph.add_edge('4', '3')



# bokeh.show()