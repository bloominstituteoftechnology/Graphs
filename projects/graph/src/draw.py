"""
General drawing methods for graphs using Bokeh.
"""
import math
import random
from graph import Graph

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Circle
from bokeh.palettes import Spectral8


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph, title="Bokeh graph", width=600, height=600):
        self.graph = graph
        self.title = title
        self.width = width
        self.height = height
        self.x_range = (0, width)
        self.y_range = (0, height)
        # List of vertex labels
        # self.vertices = [int(x) for x in self.graph.vertices.keys()]

        # self.bokeh_graph = GraphRenderer()
        # print(f'''VERTICES TREE {self.verticesSET}''')

        N = len( graph.vertices )
        node_indices = list(graph.vertices.keys())

        print(node_indices)

        plot = figure(title="Graph Layout Demonstration", x_range=(-7,7), y_range=(-7,7),
                      tools="", toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        # node_colors = ['red'] * N
        # graph.node_renderer.data_source.add(node_colors, 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color="red")

        edge_start = []
        edge_end = []

        # O(E), where E is the total number of edges
        for vertex_id in node_indices:
            for v in graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(v)

        graph_renderer.edge_renderer.data_source.data = dict(
            # start=[0]*N,
            # end=node_indices)
            start=edge_start,
            end=edge_end)

        # d = dict(
        #     start=[0]*N,
        #     end=node_indices)
        # print(d)

        ### start of layout code
        # circ = [i*2*math.pi/8 for i in node_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]
        x = []
        y = []
        for key in node_indices:
            #for vertex_id in node_indices:
            vertex = graph.vertices[key]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        output_file('graph.html')
        show(plot)

graph = Graph() # Instantiate your graph
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
# print(graph.vertices)
# bg = BokehGraph(graph)



