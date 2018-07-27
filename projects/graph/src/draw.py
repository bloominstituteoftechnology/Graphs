"""
General drawing methods for graphs using Bokeh.
"""

import math
import random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (
    GraphRenderer, StaticLayoutProvider,
    Circle, LabelSet, ColumnDataSource,
    Oval, MultiLine, HoverTool, TapTool, BoxSelectTool)
from bokeh.models.graphs import (
    NodesAndLinkedEdges,
    EdgesAndLinkedNodes
)

from bokeh.palettes import Spectral4
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
        # print(f'''VERTICES TREE {self.verticesSET}''')

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
        plot.add_tools(HoverTool(tooltips=None), TapTool(), BoxSelectTool())
        self.define_vertex_shape()
        self.define_edges()
        self.bokeh_graph.selection_policy = NodesAndLinkedEdges()
        self.bokeh_graph.inspection_policy = EdgesAndLinkedNodes()

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
        connected_components = self.graph.connected_components  # Is a list

        # define Vertex shape and color
        self.bokeh_graph.node_renderer.glyph = Oval(
            width=10, height=10, fill_color="fill_color"
        )

        # Get colors for each connected component.
        colors = self._get_random_colors(len(connected_components))

        # MAP vertex (that belongs to a Component) to its color
        vertex_color_map = {
            'index': self.vertices,
            'fill_color': [0] * len(self.vertices)
        }
        # print(f'''
        # Colors Len: {len(colors)}
        # Connected_components Len: {len(connected_components)}
        # Vertex_color_map: {vertex_color_map}
        # ''')

        # Assign to each connected component a unique single color.
        for i in range(len(colors)):
            color = colors[i]
            component = connected_components[i]
            for vertex in component:
                vertex_color_map['fill_color'][int(vertex)] = color

        self.bokeh_graph.node_renderer.data_source.data = vertex_color_map

    def define_edges(self):
        start = []
        end = []
        for key in self.vertices:

            # Make a copy of the edges in roder to preserve the integrity of
            # the Graph
            connected_nodes = self.graph.vertices[str(key)].copy()

            # If there are Edges for the current looped Vertex
            if len(connected_nodes):
                for i in range(len(connected_nodes)):
                    start.append(key)  # Add node
                    end.append(int(connected_nodes.pop()))  # Add related edge
            #     print(start)
            #     print(end)
            # print(self.graph.vertices[str(key)])

        color = ['#111111']*len(start)
        self.bokeh_graph.edge_renderer.data_source.data = dict(
            start=start, end=end,
        )
        self.bokeh_graph.edge_renderer.glyph = MultiLine(
            line_color="#CCCCCC", line_alpha=0.8, line_width=1)
        self.bokeh_graph.edge_renderer.selection_glyph = MultiLine(
            line_color=Spectral4[2], line_width=3)
        self.bokeh_graph.edge_renderer.hover_glyph = MultiLine(
            line_color=Spectral4[1], line_width=3)
        print(self.bokeh_graph.edge_renderer.data_source.data.keys())

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
