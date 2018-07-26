"""
General drawing methods for graphs using Bokeh.
"""

import random
from random import choice, random, uniform
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=10, height=10, show_axis=False, show_grid=False, circle_size=35):
        if not graph.vertices:
            raise Exception('Graph must have vertices')
        self.graph = graph

        self.width = width
        self.height = height
        self.pos = {}
        self.plot = figure(title=title, x_range=(0,width), y_range=(0, height))

        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(list(self.graph.vertices.keys()), 'index')
        # graph_renderer.node_renderer.data_source.add(self._get_random_colors(), 'color')
        graph_renderer.node_renderer.data_source.add(self._color_connected_components(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size, fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.plot.add_layout(self._draw_labels())
        self.plot.renderers.append(graph_renderer)

    def _draw_labels(self):
        xs = []
        ys = []
        vertex_labels = []

        for vertex, position in self.pos.items():
            xs.append(position[0])
            ys.append(position[1])
            vertex_labels.append(vertex)

        source = ColumnDataSource(data=dict(xs=xs, ys=ys, vertex_labels=vertex_labels))

        labels = LabelSet(x='xs', y='ys', text='vertex_labels', text_align='center', text_baseline='middle', text_color='white', text_font_size= '20pt', source=source)

        return labels

    def _color_connected_components(self):
        vertex_colors_dict = dict((vertex, 'black') for vertex in list(self.graph.vertices.keys()))
        
        for vertex in vertex_colors_dict:
            if vertex_colors_dict[vertex] is 'black':
                rand_color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
                vertex_colors_dict[vertex] = rand_color
                for connected_node in self.graph.search(start=vertex):
                    vertex_colors_dict[connected_node] = rand_color
        
        colors = []
        for vertex, color in vertex_colors_dict.items():
            colors.append(color)

        # print (colors)
        return colors

    def _get_random_colors(self):
        colors = []
        for _ in range(len(self.graph.vertices)):
            color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors

    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.append(vertex)
                    end_indices.append(destination)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.graph.vertices:
            randomx = 1 + random() * (self.width - 2)
            randomy = 1 + random() * (self.height - 2)
            self.pos[vertex] = (randomx, randomy)
