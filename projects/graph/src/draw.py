

import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
# from bokeh.palettes import Spectral8
from graph import Graph

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)



node_indices = list(graph.vertices)
l = len(graph.vertices)
print(node_indices)
plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10), y_range=(-1.1,10),
              tools='', toolbar_location=None)

graph_renderer = GraphRenderer()  

graph_renderer.node_renderer.data_source.add(node_indices, 'index')
graph_renderer.node_renderer.data_source.add(['red']*l, 'color')
graph_renderer.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

start_i = []
end_i = []

for vertex in graph.vertices:
  for end_point in graph.vertices[vertex]:
    start_i.append(vertex)
    end_i.append(end_point)

print(start_i)
print(end_i)


graph_renderer.edge_renderer.data_source.data = dict(
    start=start_i,
    end=end_i)

### start of layout code
square = [int(v) for v in graph.vertices]
x = [2 * (i//3) for i in square]
# x = [i for i in circ]
# y = [i for i in circ]
y = [2 * (i % 3) for i in square]

print(x, y)

graph_layout = dict(zip(node_indices, zip(x, y)))
print(graph_layout)
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph_renderer)

output_file('graph.html')
show(plot)
