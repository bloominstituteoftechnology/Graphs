"""
General drawing methods for graphs using Bokeh.
"""
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle
from graph import Graph

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_edge('4', '1')
graph.add_edge('2', '3')

print(graph.vertices)


N = len(graph.vertices)
node_indices = list(graph.vertices)

plot = figure(title="Graph Layout Demonstration", x_range=(-1.1,10.1), y_range=(-1.1,10.1),
              tools="", toolbar_location=None)

graphs = GraphRenderer()

graphs.node_renderer.glyph = Circle(radius=0.5, fill_color='color')
graphs.node_renderer.data_source.add(node_indices, 'index')
graphs.node_renderer.data_source.add(['red'] * N, 'color')

start_indices = []
end_indices = []

for vertex in graph.vertices:
    for edge_end in graph.vertices[vertex]:
        start_indices.append(vertex)
        end_indices.append(edge_end)

graphs.edge_renderer.data_source.data = dict(
    start = start_indices,
    end = end_indices
)

circ = [int(v) for v in graph.vertices]
x = [2 * (i // 3) for i in circ]
y = [2 * (i % 3) for i in circ]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout = graph_layout)

plot.renderers.append(graph_renderer)

output_file('graph.html')
show(plot)

