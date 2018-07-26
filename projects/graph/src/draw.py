"""
General drawing methods for graphs using Bokeh.
"""

import math
from random import choice
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, MultiLine, LabelSet, ColumnDataSource

class BokehGraph:
  """Class that takes a graph and exposes drawing methods."""
  def __init__(self, graph):
    self.graph = graph

    self.width = 15
    self.height = 15
    self.plot = figure(title="Graph Demo",
                      x_range=(-self.width, self.width),
                      y_range=(-self.height, self.height),
                      tools="",
                      toolbar_location=None)
    self.plot.axis.visible = False
    self.render()

  def render(self):
    node_indices = list(self.graph.vertices.keys())
    N = len(node_indices)

    graph_renderer = GraphRenderer()
    graph_renderer.node_renderer.data_source.add(node_indices, 'index')
    graph_renderer.node_renderer.data_source.add(self.random_colors(N), 'color')
    graph_renderer.node_renderer.glyph = Circle(radius=1.0, fill_color="color")

    edges, num_of_edges = self._edges()
    graph_renderer.edge_renderer.data_source.data = edges
    graph_renderer.edge_renderer.data_source.add(self.random_colors(num_of_edges), 'color')
    graph_renderer.edge_renderer.glyph = MultiLine(line_color='color')

    self.coordinates = self._generate_coordinates(node_indices)
    graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.coordinates)
    self.plot.renderers.append(graph_renderer)

  def show(self):
    output_file("output.html")
    show(self.plot)

  def _edges(self):
    start = []
    end = []
    for v, edges in self.graph.vertices.items():
      for e in edges:
        start.append(v)
        end.append(e)

    return dict(start=start, end=end), len(start)

  def _generate_coordinates(self, node_indices):
    circ = [i*2*math.pi/8 for i in list(map(int, node_indices))]
    x = [0.75*self.width*math.cos(i) for i in circ]
    y = [0.75*self.height*math.sin(i) for i in circ]
    return dict(zip(node_indices, zip(x, y)))

  def random_color(self):
    return '#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)])

  def random_colors(self, count):
    return [self.random_color() for _ in range(count)]