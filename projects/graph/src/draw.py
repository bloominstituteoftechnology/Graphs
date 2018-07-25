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
# import graph


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
        self.vertices = [*self.graph.vertices.keys()]
        self.verticesSET = set([*self.graph.vertices.keys()])
        self.bokeh_graph = GraphRenderer()
        print(f'''VERTICES TREE {self.verticesSET}''')

    def show(self):
        '''Paint the graph object'''

        plot = figure(
            plot_width=self.width,
            plot_height=self.height,
            title=self.title,
            x_range=(0, self.width),
            y_range=(0, self.height)
        )
        plot.axis.visible = False
        plot.grid.visible = False
        self.define_vertex_shape()
        self.define_edges()
        self.map_to_coordinates()

        # print('\nSHAPE', self.bokeh_graph.node_renderer.data_source.data)
        # print('\nEDGES', self.bokeh_graph.edge_renderer.data_source.data)
        # print('\nCOORDINATES', self.bokeh_graph.layout_provider)
        # INCLUDE the Graph in the Plot
        plot.renderers.append(self.bokeh_graph)
        # GENERATE PLOT HTML FILE AND OPEN IN BROWSER
        output_file('./graph.html')
        show(plot)

    def define_vertex_shape(self):
        # Get Connected components
        self.graph.bfs()
        connected_components = self.graph.connected_components

        # define Vertex shape and color
        self.bokeh_graph.node_renderer.glyph = Oval(
            width=15, height=15, fill_color="fill_color"
        )

        # Get colors for each connected component.
        colors = self._get_random_colors(len(connected_components))

        # MAP vertex to its color
        vertex_color = {
            'index': self.vertices,
            'fill_color': [0] * len(self.vertices)
        }
        print(f'''Colors: {colors}
        colors Len: {len(colors)}
        connected_components Len: {len(connected_components)}
        Vertex_colors: {vertex_color}
        ''')

        # Assign to each connected component a unique single color.
        for i in range(len(colors)):
            color = colors[i]
            component = connected_components[i]
            for vertex in component:
                vertex_color['fill_color'][int(vertex)] = color

        self.bokeh_graph.node_renderer.data_source.data = vertex_color

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

    def _get_random_colors(self, number):
        colors = []
        for _ in range(number):
            color = '#'+''.join(
                [random.choice('0123456789ABCDEF') for j in range(6)]
            )
            colors.append(color)
        return colors
