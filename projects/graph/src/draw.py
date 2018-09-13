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
        self.vertices = list(graph.vertices.keys())      
        self.graphIn = graph
    def show(self):
        node_indices = self.vertices       
        plot = figure(title='Graph Layout Demonstration', x_range=self.graphIn.x_range, y_range=self.graphIn.y_range,
              tools='', toolbar_location=None)
              
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add([self.graphIn.vertices[vertex_id].color for vertex_id in self.graphIn.vertices], 'color')
        graph.node_renderer.glyph = Circle(radius=self.graphIn.circle_radius, fill_color='color', name=str(node_indices))
        
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
        if self.graphIn.labels:
            data = {
                    'x': x,
                    'y': y,
                    'name': node_indices
                }
            source = ColumnDataSource(data)
            labels = LabelSet(x="x", y="y", text="name", y_offset = -7,
                            text_font_size="8pt", text_color="white",
                            source=source, text_align='center')

            plot.add_layout(labels)
        plot.renderers.append(graph)

        output_file('graph2.html')
        show(plot)

graph = Graph()

for i in range(10):
    graph.add_vertex(i)

graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(5,6)
graph.add_edge(0,6)
graph.add_edge(0,7)
graph.add_edge(7,8)
graph.add_edge(8,9)

b_graph = BokehGraph(graph)

b_graph.show()

