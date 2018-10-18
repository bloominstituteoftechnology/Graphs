"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, Oval, LabelSet,
                          ColumnDataSource, Arrow, NormalHead)
from bokeh.palettes import Spectral8
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        self.graph = graph

    def draw(self):
        graph = self.graph

        N = len(graph.vertices)
        node_indices = list(graph.vertices.keys())

        plot = figure(title="Graph Layout Demonstration", x_range=(-7, 7), y_range=(-7, 7),
                      tools="", toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        # changes color of nodes
        node_colors = ['red'] * N
        # graph_renderer.node_renderer.data_source.add(node_colors, 'color')
        graph_renderer.node_renderer.data_source.add(Spectral8, 'color')

        graph_renderer.node_renderer.glyph = Circle(
            radius=0.5, fill_color="color")


        edge_start = []
        edge_end = []

        # O(E), where E is the total number of edges
        for vertex_id in node_indices:
            for v in graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(v)

        # print("EDGES:")
        # print(edge_start)
        # print(edge_end)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)

        # start of layout code
        # circ = [i*2*math.pi/8 for i in node_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]
        x = []
        y = []
        for vertex_id in node_indices:
            vertex = graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        print("X,Y:")
        print(x, y)

        # for value_x in x:
        #     for value_y in y:
        #         plot.add_layout(Arrow(end=NormalHead(fill_color="orange"), x_start=value_x, y_start=value_y, x_end=0.5, y_end=0.7))

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[vertex_id for vertex_id in graph.vertices]))
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                     text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('5')
# graph.add_vertex('2')
# graph.add_vertex('6')
# graph.add_vertex('1')
# graph.add_vertex('4')
# graph.add_vertex('7')
# graph.add_vertex('3')
# graph.add_vertex('99')

# graph.add_edge('5', '2')
# graph.add_edge('5', '6')
# graph.add_edge('2', '1')
# graph.add_edge('2', '4')
# graph.add_edge('4', '3')
# graph.add_edge('6', '7')


# print(graph.vertices)

# print(graph.dft('5'))
# print(graph.bft('5'))

# # help(graph.add_edge)

# bg = BokehGraph(graph)
# bg.draw()
