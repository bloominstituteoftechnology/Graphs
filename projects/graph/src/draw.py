"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph
import random


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        if not graph.vertices:
            raise Exception("Graph should contain vertices")
        self.graph = graph
        self.pos = {}

    def _get_edges(self):
        start = []
        end = []
        checked = set()
        for startpoint, endpoints in self.graph.vertices.items():
            for endpoint in endpoints:
                if (startpoint, endpoint) not in checked:
                    checked.add((startpoint, endpoint))
                    start.append(startpoint)
                    end.append(endpoint)
        return dict(start=start, end=end)

    def _get_random_colors(self):
        colors = []
        for vertex in self.graph.vertices:
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            colors.append(color)
        return colors

    def map_coords(self):
        for vertex in self.graph.vertices.keys():
            self.pos[vertex] = (random.uniform(0.5,9.5), random.uniform(0.5,9.5))
        
    def draw(self, title='Graph', width=10, height=10,
                show_axis=False, show_grid=False, circle_size=35):
        plot = figure(title=title, x_range=(0,width), y_range=(0,height))
        
        plot.axis.visible = show_axis
        plot.grid.visible = show_grid

        graph = GraphRenderer()
        graph.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        graph.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        graph.node_renderer.glyph = Circle(size=circle_size,
            fill_color='color')
        graph.edge_renderer.data_source.data = self._get_edges()

        self.map_coords()
        graph.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        plot.renderers.append(graph)

        output_file('./graph.html')
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
graph.add_edge('0', '7')
graph.add_edge('1', '6', bidirectional=False)
graph.add_edge('3', '6')
graph.add_edge('6', '7')
graph.add_edge('0', '5')
graph.add_edge('4', '2')
print(graph.vertices)

bokeh = BokehGraph(graph)
bokeh.draw()