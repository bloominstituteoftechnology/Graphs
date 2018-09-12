# """
# General drawing methods for graphs using Bokeh.
# """
#
# from graph import Graph, Vertex
# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
#                           ColumnDataSource)
#
#
# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#     def __init__(self, graph, title='Graph', width=100, height=100, show_axis=False, show_grid=False, circle_size=35, draw_components=False):
#         if not graph.vertices:
#             raise Exception('Error: Graph has no vertices!')
#         self.graph = graph
#         self.width = width
#         self.height = height
#         self.pos = {}
#
#         self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
#         self.plot.axis.visible = show_axis
#         self.plot.grid.visible = show_grid
#         self._setup_graph_renderer(circle_size, draw_components)
#         self._setup_labels()
#
#
#     def _setup_graph_renderer(self, circle_size, draw_components):
#         graph_renderer = GraphRenderer()
#         self.vertex_list = list(self.graph.vertices.keys())
#
#         graph_renderer.node_renderer.data_source.add(
#             [vertex.label for vertex in self.vertex_list], 'index')
#         colors = (self._get_connected_component_colors() if draw_components
#             else self._get_random_colors())
#         graph_renderer.node_renderer.data_source.add(colors, 'color')
#
#         graph_renderer.node_renderer.glyph = Circle(size=circle_size, fill_color='color')
#
#         graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
#         self.randomize()
#         graph_renderer.layout_provider = StaticLayoutProvider(graph_layout = self.pos)
#         self.plot.renderers.append(graph_renderer)
#
#     def _get_edge_indexes(self):
#         start_indices = []
#         end_indices = []
#         checked = set()
#
#         for vertex, edges in self.graph.vertices.items():
#             if vertex not in checked:
#                 for destination in edges:
#                     start_indices.append(vertex.label)
#                     end_indices.append(destination.label)
#                 checked.add(vertex)
#
#         return dict(start=start_indices, end=end_indices)

import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet
from bokeh.palettes import Spectral8
from graph import Graph



graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('9')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '6')
graph.add_edge('0', '8')
graph.add_edge('0', '9')
print(graph.vertices)

N = len(graph.vertices)
node_indices = list(graph.vertices)





plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1), y_range=(-1.1,10.1),
              tools='', toolbar_location=None)

graph_renderer = GraphRenderer()

graph_renderer.node_renderer.data_source.add(node_indices, 'index')
graph_renderer.node_renderer.data_source.add(['red', 'blue', 'green', 'orange', 'purple', 'red', 'magenta', 'tan', 'gray', 'yellow'], 'color')
graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

start_indices = []
end_indices = []

for vertex in graph.vertices:
    for edge_end in graph.vertices[vertex]:
        start_indices.append(vertex)
        end_indices.append(edge_end)
print(start_indices)
print(end_indices)


graph_renderer.edge_renderer.data_source.data = dict(
    start=start_indices,
    end=end_indices)

### start of layout code
grid = [int(v) for v in graph.vertices]
x = [2 * (i // 3) for i in grid]
y = [2 * (i % 3) for i in grid]
# x = [i for i in grid]
# y = [i ** 2 for i in grid]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph_renderer)

labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
labels = LabelSet(x='x', y='y', text='names', level='glyph',
             text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')


plot.add_layout(labels)


output_file('graph.html')
show(plot)
