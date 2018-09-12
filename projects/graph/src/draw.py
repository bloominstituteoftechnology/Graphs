from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider,
                          Circle, LabelSet, ColumnDataSource)
from bokeh.palettes import Viridis10
import math
from graph import Graph


class BokehGraph:
    def __init__(self, graph):
        self.vertices = list(graph.vertices.keys())  # [0,1,2]
        self.graphIn = graph

    def show(self):
        node_indices = self.vertices
        plot = figure(title='Graph Layout Demonstration',
                      x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
                      tools='', toolbar_location=None)

        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Viridis10, 'color')
        graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color',
                                           name=str(node_indices))

        starts = []
        for k in self.graphIn.vertices.keys():
            starts += [k]*(len(self.graphIn.vertices[k]))
        ends = []
        for k, v in self.graphIn.vertices.items():
            ends += v
        graph.edge_renderer.data_source.data = dict(
            start=starts,
            end=ends)

        circ = [int(i)*2*math.pi/len(self.vertices) for i in node_indices]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        # setup labels
        data = {
                'x': x,
                'y': y,
                'name': node_indices
            }
        source = ColumnDataSource(data)
        labels = LabelSet(x="x", y="y", text="name", y_offset=-5,
                          text_font_size="12pt", text_color="white",
                          source=source, text_align='center')

        plot.add_layout(labels)
        plot.renderers.append(graph)

        output_file('graph2.html')
        show(plot)


graph = Graph()

graph.add_vertex('0')
graph.add_vertex('1')

graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('4', '2')
graph.add_edge('1', '4')
graph.add_edge('5', '3')
graph.add_edge('6', '3')
graph.add_edge('7', '4')

bokeh = BokehGraph(graph)

bokeh.show()
