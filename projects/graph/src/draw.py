"""
General drawing methods for graphs using Bokeh.
"""

import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet
from bokeh.palettes import Spectral8
from graph import Graph
from graph import dft
from graph import dfs
from graph import bft




graph = Graph()  # Instantiate your graph

#Vertices
for i in range(0, 10):
    graph.add_vertex(str(i))

#Edges
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
graph.add_edge('2', '5')
graph.add_edge('2', '4')
graph.add_edge('4', '9')
graph.add_edge('3', '7')
graph.add_edge('3', '6')

# graph.add_edge('0', '8')
# graph.add_edge('8', '128')
# graph.add_edge('128', '120')
# graph.add_edge('120', '0')

# graph.add_edge('8', '100')
# graph.add_edge('0', '96')
# graph.add_edge('120', '156')
# graph.add_edge('128', '160')


# graph.add_edge('96', '100')
# graph.add_edge('100', '160')
# graph.add_edge('160', '156')
# graph.add_edge('156', '96')

# graph.add_edge('100', '146')
# graph.add_edge('96', '144')
# graph.add_edge('156', '174')
# graph.add_edge('160', '176')

# graph.add_edge('144', '146')
# graph.add_edge('146', '176')
# graph.add_edge('176', '174')
# graph.add_edge('174', '144')

# dft(graph.vertices, '8', [])
# dfs(graph.vertices, '8', [], '128')
# graph.bft(graph.vertices, '0')




#print(graph.vertices)


N = len(graph.vertices)
node_indices = list(graph.vertices)


plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1), y_range=(-1.1,10.1),
              tools='', toolbar_location=None)

graph_renderer = GraphRenderer()

graph_renderer.node_renderer.data_source.add(node_indices, 'index')
graph_renderer.node_renderer.data_source.add([graph.vertices[vertex_id].color for vertex_id in graph.vertices], 'color')
graph_renderer.node_renderer.glyph = Circle(radius=0.4, fill_color='color')

start_indices = []
end_indices = []

for vertex_id in graph.vertices:
    for edge_end in graph.vertices[vertex_id].edges:
        start_indices.append(vertex_id)
        end_indices.append(edge_end)
# print(start_indices)
# print(end_indices)


graph_renderer.edge_renderer.data_source.data = dict(
    start=start_indices,
    end=end_indices)

### start of layout code
x = [graph.vertices[vertex_id].x for vertex_id in graph.vertices]
y = [graph.vertices[vertex_id].y for vertex_id in graph.vertices]

# x = [50 * (i // 15) for i in grid]
# y = [50 * (i % 15) for i in grid]


graph_layout = dict(zip(node_indices, zip(x, y)))
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph_renderer)

labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[graph.vertices[vertex_id].value for vertex_id in graph.vertices]))
labels = LabelSet(x='x', y='y', text='names', level='glyph',
text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')


plot.add_layout(labels)


output_file('graph.html')
show(plot)
