"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)
import math
from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.vertices = list(graph.vertices.keys()) # [0,1,2]        
        self.graphIn = graph
    def show(self):
        node_indices = self.vertices       
        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,610.1), y_range=(600.1, -1.1),
              tools='', toolbar_location=None)
              
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add([self.graphIn.vertices[vertex_id].color for vertex_id in self.graphIn.vertices], 'color')
        graph.node_renderer.glyph = Circle(radius=1.5, fill_color='color', name=str(node_indices))
        
        start_indices = []
        end_indices = []

        for vertex in self.graphIn.vertices:
            for edge_end in self.graphIn.vertices[vertex].edges:
                start_indices.append(vertex)
                end_indices.append(edge_end)

        graph.edge_renderer.data_source.data = dict(
            start= start_indices,
            end= end_indices,
            )

        x = [self.graphIn.vertices[vertex_id].x for vertex_id in self.graphIn.vertices]
        y = [self.graphIn.vertices[vertex_id].y for vertex_id in self.graphIn.vertices]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        #setup labels
        # data = {
        #         'x': x,
        #         'y': y,
        #         'name': node_indices
        #     }
        # source = ColumnDataSource(data)
        # labels = LabelSet(x="x", y="y", text="name", y_offset = -7,
        #                 text_font_size="8pt", text_color="white",
        #                 source=source, text_align='center')

        # plot.add_layout(labels)
        plot.renderers.append(graph)

        output_file('graph2.html')
        show(plot)
