"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource, Oval
from bokeh.palettes import Spectral4
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graph = self.graph

        N = len(self.graph.vertices)
        node_indices = list(self.graph.vertices.keys())

        plot = figure(title="Graph Layout Demonstration", x_range=(-6,6), y_range=(-6,6),
                    tools="", toolbar_location=None)

        graph_render = GraphRenderer()

        graph_render.node_renderer.data_source.add(node_indices, 'index')
        node_colors = ['red'] * int(N / 2)
        another_color = ['blue'] * int(N/2)
        node_colors.extend(another_color)
        if N % 2 != 0:
            node_colors.extend(['green'])
        graph_render.node_renderer.data_source.add(node_colors, 'color')
        graph_render.node_renderer.glyph = Circle(radius=0.2, fill_color="color")

        edge_start = []
        edge_end = []

        for vert_id in node_indices:
            for v in graph.vertices[vert_id].edges:
                edge_start.append(vert_id)
                edge_end.append(v)

        graph_render.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)

        ### start of layout code
        # circ = [i*2*math.pi/8 for i in node_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]
        x = []
        y = []
        for vert_id in node_indices:
            vertex = graph.vertices[vert_id]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_render.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        ### Draw quadratic bezier paths
        # def bezier(start, end, control, steps):
        #     return [(1-s)**2*start + 2*(1-s)*s*control + s**2*end for s in steps]

        # xs, ys = [], []
        # sx, sy = graph_layout[0]
        # steps = [i/100. for i in range(100)]
        # for node_index in node_indices:
        #     ex, ey = graph_layout[node_index]
        #     xs.append(bezier(sx, ex, 0, steps))
        #     ys.append(bezier(sy, ey, 0, steps))
        # graph.edge_renderer.data_source.data['xs'] = xs
        # graph.edge_renderer.data_source.data['ys'] = ys

        plot.renderers.append(graph_render)

        output_file("graph_demo.html")
        show(plot)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')


# bg = BokehGraph(graph)
# bg.draw()