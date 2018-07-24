"""
General drawing methods for graphs using Bokeh.
"""

import math
import random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (
    GraphRenderer, StaticLayoutProvider,
    Circle, LabelSet, ColumnDataSource, Oval)
import graph


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
        self.vertices = [int(x) for x in self.graph.vertices.keys()]
        self.bokeh_graph = GraphRenderer()
        self.show()

    def show(self):
        '''Paint the graph object'''

        plot = figure(plot_width=self.width,
                      plot_height=self.height,
                      title=self.title,
                      x_range=(0, self.width),
                      y_range=(0, self.height)
                      )
        self.define_vertex_shape()
        self.define_edges()
        self.map_to_coordinates()

        print('\nSHAPE', self.bokeh_graph.node_renderer.data_source.data)
        print('\nEDGES', self.bokeh_graph.edge_renderer.data_source.data)
        print('\nCOORDINATES', self.bokeh_graph.layout_provider)
        # INCLUDE the Graph in the Plot
        plot.renderers.append(self.bokeh_graph)
        # GENERATE PLOT HTML FILE AND OPEN IN BROWSER
        output_file('./graph.html')
        show(plot)

    def define_vertex_shape(self):
        # define Vertex shape and color
        self.bokeh_graph.node_renderer.glyph = Oval(
            width=10, height=10, fill_color="fill_color"
        )
        # MAP vertex to its color
        self.bokeh_graph.node_renderer.data_source.data = dict(
            index=self.vertices, fill_color=self._get_random_colors())

    def define_edges(self):
        start = []
        end = []
        for key in self.vertices:

            # Make a copy of the edges in roder to preserve the integrity of the Graph
            connected_nodes = self.graph.vertices[str(key)].copy()

            if len(connected_nodes):  # If there are Edges for the current looped Vertex
                for i in range(len(connected_nodes)):
                    start.append(key)  # Add node
                    end.append(int(connected_nodes.pop()))  # Add related edge
            #     print(start)
            #     print(end)
            # print(self.graph.vertices[str(key)])

        self.bokeh_graph.edge_renderer.data_source.data = dict(
            start=start, end=end
        )

    def map_to_coordinates(self):
        # Define random coordintes for each node
        x = [random.randint(10, self.width - 10) for _ in self.vertices]
        y = [random.randint(10, self.height - 10) for _ in self.vertices]

        # MAP vertex to its coordinates
        coordinates = dict(zip(self.vertices, zip(x, y)))
        print(coordinates)

        self.bokeh_graph.layout_provider = StaticLayoutProvider(
            graph_layout=coordinates)

    def _get_random_colors(self):
        colors = []
        for _ in range(len(self.graph.vertices)):
            color = '#'+''.join([random.choice('0123456789ABCDEF')
                                 for j in range(6)])
            colors.append(color)
        return colors


_graph = graph.Graph()  # Instantiate your graph
_graph.add_vertex('0')
_graph.add_vertex('1')
_graph.add_vertex('2')
_graph.add_vertex('3')
_graph.add_vertex('4')
_graph.add_vertex('5')
_graph.add_vertex('6')
_graph.add_vertex('7')
_graph.add_edge('0', '1')
_graph.add_edge('0', '3')
# print(_graph.vertices)
# graph.add_edge('0', '4')

bokeh_graph = BokehGraph(_graph)
# print(bokeh_graph)
