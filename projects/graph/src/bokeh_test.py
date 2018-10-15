import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle
from bokeh.palettes import Spectral4
from graph import Graph

g = Graph()
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_vertex('7')
g.add_edge('0', '1')
g.add_edge('0', '3')
g.add_edge('0', '5')
g.add_edge('0', '7')
g.add_edge('2', '5')
g.add_edge('3', '4')
g.add_edge('6', '5')
g.add_edge('2', '6')
node_indices = list(g.vertices.keys())

plot = figure(title='Graph Layout Demonstration', x_range=(-1, 6),
              y_range=(-1, 6), tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.glyph = Circle(size=30, fill_color='green')

graph.edge_renderer.data_source.data = dict(
    start=node_indices,
    end=[list(g.vertices[v].edges) for v in g.vertices])

names = []
x = []
y = []
for vertex in g.vertices:
    names.append(g.vertices[vertex].label)
    x.append(g.vertices[vertex].x)
    y.append(g.vertices[vertex].y)

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
