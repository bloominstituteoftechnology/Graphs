import math
import graph

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Circle
from bokeh.palettes import Spectral8
from graph import Graph


graph = Graph()  # Instantiate your graph
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
print(graph.vertices)

N = len(graph.vertices)
node_indices = list(graph.vertices)


plot = figure(title='Graph Layout Demonstration', x_range=(-1.1, 10.1), y_range=(-1.1, 10.1),
              tools='', toolbar_location=None)

graph_renderer = GraphRenderer()

graph_renderer.node_renderer.data_source.add(node_indices, 'index')
graph_renderer.node_renderer.data_source.add(
    [graph.vertices[vertex_id].color for vertex_id in graph.vertices], 'color')
graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

start_indices = []
end_indices = []

for vertex_id in graph.vertices:
    for edge_end in graph.vertices[vertex_id].edges:
        start_indices.append(vertex_id)
        end_indices.append(edge_end)

print(start_indices)
print(end_indices)

graph_renderer.edge_renderer.data_source.data = dict(
    start=start_indices,
    end=end_indices)

# start of layout code
circ = [int(v) for v in graph.vertices]
x = [graph.vertices[vertex_id].x for vertex_id in graph.vertices]
y = [graph.vertices[vertex_id].y for vertex_id in graph.vertices]


graph_layout = dict(zip(node_indices, zip(x, y)))
graph_renderer.layout_provider = StaticLayoutProvider(
    graph_layout=graph_layout)

plot.renderers.append(graph_renderer)

output_file('graph.html')
show(plot)
