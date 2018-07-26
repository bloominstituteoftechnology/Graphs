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
  def __init__(self, graph, connected_components=False):
    self.graph = graph

    self.connected_components = connected_components
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
    graph_renderer = GraphRenderer()

    node_indices, node_colors = self._indices_and_colors()
    graph_renderer.node_renderer.data_source.add(node_indices, 'index')
    graph_renderer.node_renderer.data_source.add(node_colors, 'color')
    graph_renderer.node_renderer.glyph = Circle(radius=1.0, fill_color="color")

    edges, edge_colors = self._edges_and_colors()
    graph_renderer.edge_renderer.data_source.data = edges
    graph_renderer.edge_renderer.data_source.add(edge_colors, 'color')
    graph_renderer.edge_renderer.glyph = MultiLine(line_color='color')

    self.coordinates = self._generate_coordinates(node_indices)
    graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.coordinates)
    self.plot.renderers.append(graph_renderer)

    self.plot.add_layout(self._labels())

  def show(self):
    output_file("output.html")
    show(self.plot)

  def _indices_and_colors(self):
    if not self.connected_components:
      node_indices = [v.label for v in self.graph.vertices]
      return node_indices, self._random_colors(len(node_indices))

    self.component_colors = self._random_colors(self.graph.connected_components())
    node_indices = []
    node_colors = []
    for v in self.graph.vertices:
      node_indices.append(v.label)
      node_colors.append(self.component_colors[v.component])

    return node_indices, node_colors

  def _edges_and_colors(self):
    start = []
    end = []
    edge_colors = []
    for v, edges in self.graph.vertices.items():
      for each in edges:
        start.append(v.label)
        end.append(each.label)
        edge_colors.append(self.component_colors[v.component] if self.connected_components else self._random_color())

    return dict(start=start, end=end), edge_colors

  def _generate_coordinates(self, node_indices):
    circ = [i*2*math.pi/len(node_indices) for i in list(map(int, node_indices))]
    x = [0.75*self.width*math.cos(i) for i in circ]
    y = [0.75*self.height*math.sin(i) for i in circ]
    return dict(zip(node_indices, zip(x, y)))

  def _labels(self):
    data = {'x': [], 'y': [], 'labels': []}
    for v, coordinate in self.coordinates.items():
      data['x'].append(coordinate[0])
      data['y'].append(coordinate[1])
      data['labels'].append(str(v))
    return LabelSet(x='x', y='y', text='labels', level='glyph',
                    text_align='center', text_baseline='middle', source=ColumnDataSource(data), render_mode='canvas')

  def _random_color(self):
    return '#' + ''.join([choice('0123456789ABCDEF') for _ in range(6)])

  def _random_colors(self, count):
    return [self._random_color() for _ in range(count)]