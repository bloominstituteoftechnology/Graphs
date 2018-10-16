# """
# General drawing methods for graphs using Bokeh.
# """

# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
#                           ColumnDataSource)

# graph = {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }

# p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# p.line(x, y, legend="Temp.", line_width=2)

# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#     def __init__(self):
#         pass  # TODO

import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8
from graph import Graph

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)

N = len(graph.vertices)
node_indices = list(graph.vertices)

plot = figure(
    title="Graph Layout Demonstration",
    x_range=(-1.1, 10.1),
    y_range=(-1.1, 10.1),
    tools="",
    toolbar_location=None,
)

graph_renderer = GraphRenderer()

graph_renderer.node_renderer.data_source.add(node_indices, "index")
graph_renderer.node_renderer.data_source.add(Spectral8, "color")
graph_renderer.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color="color")

start_indices = []
end_indices = []

for vertex in graph.vertices:
    for edge_end in graph.vertices[vertex]:
        start_indices.append(vertex)
        end_indices.append(edge_end)

graph_renderer.edge_renderer.data_source.data = dict(
    start=start_indices, 
    end=end_indices)

### start of layout code
circ = [int(v) for v in graph.vertices]
print("circ ", circ)
x = [2 * (i // 3) for i in circ]
y = [2 * (i % 3) for i in circ]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph_renderer)

output_file("graph.html")
show(plot)
