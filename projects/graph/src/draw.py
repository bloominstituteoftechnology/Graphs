# """
# General drawing methods for graphs using Bokeh.
# """

# import math 

# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, Oval, LabelSet,
#                           ColumnDataSource)
# from bokeh.palettes import Spectral8
# from graph import Graph

# graph1 = Graph()  # Instantiate your graph
# graph1.add_vertex('0')
# graph1.add_vertex('1')
# graph1.add_vertex('2')
# graph1.add_vertex('3')
# graph1.add_edge('0', '1')
# graph1.add_edge('0', '3')
# print(graph1.vertices)


# N = len(graph1.vertices)
# node_indices = list(graph1.vertices)

# plot = figure(title="Graph Layout Demonstration", x_range=(-1.1,10.1), y_range=(-1.1,10.1),
#               tools="", toolbar_location=None)

# graph_renderer = GraphRenderer()

# graph_renderer.node_renderer.data_source.add(node_indices, 'index')
# graph_renderer.node_renderer.data_source.add(['red']*N, 'color')
# graph_renderer.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

# start_indices = []
# end_indices = []

# for vertex in graph.vertices:
#     for edge_end in graph.vertices[vertex]:
#         start_indices.append(vertex)
#         end_indices.append(edge_end)

# graph_renderer.edge_renderer.data_source.data = dict(
#     start = [0] *N,
#     end = node_indices)

# ### start of layout code
# circ = [i*2*math.pi/8 for i in node_indices]
# x = [math.cos(i) for i in circ]
# y = [math.sin(i) for i in circ]

# graph_layout = dict(zip(node_indices, zip(x, y)))
# graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# plot.renderers.append(graph)

# output_file('graph.html')
# show(plot)












# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#     def __init__(self):
#         pass  # TODO





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
print(graph.vertices)

N = len(graph.vertices)
node_indices = list(graph.vertices)





plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1), y_range=(-1.1,10.1),
              tools='', toolbar_location=None)

graph_renderer = GraphRenderer()

graph_renderer.node_renderer.data_source.add(node_indices, 'index')
graph_renderer.node_renderer.data_source.add(['red', 'blue', 'green', 'orange'], 'color')
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