"""
General drawing methods for graphs using Bokeh.
"""

import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet
from bokeh.palettes import Spectral8
from graph import Graph



graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_vertex('5')
# graph.add_vertex('6')
# graph.add_vertex('7')
# graph.add_vertex('8')
# graph.add_vertex('9')
# graph.add_vertex('10')
# graph.add_vertex('11')
# graph.add_vertex('12')
# graph.add_vertex('13')
# graph.add_vertex('14')
# graph.add_vertex('15')
# graph.add_vertex('16')
# graph.add_vertex('17')
# graph.add_vertex('18')
# graph.add_vertex('19')
# graph.add_vertex('20')
# graph.add_vertex('21')
# graph.add_vertex('22')
# graph.add_vertex('23')
# graph.add_vertex('24')
# graph.add_vertex('25')
# graph.add_vertex('26')
# graph.add_vertex('27')
# graph.add_vertex('28')
# graph.add_vertex('29')
# graph.add_vertex('30')
# graph.add_vertex('31')
# graph.add_vertex('32')
# graph.add_vertex('33')
# graph.add_vertex('34')
# graph.add_vertex('35')
# graph.add_vertex('36')
# graph.add_vertex('37')
# graph.add_vertex('37')
# graph.add_vertex('38')
# graph.add_vertex('39')
# graph.add_vertex('40')
# graph.add_vertex('41')

for i in range(0, 300):
    graph.add_vertex(str(i))



# Edges
graph.add_edge('0', '8')
graph.add_edge('8', '128')
graph.add_edge('128', '120')
graph.add_edge('120', '0')

graph.add_edge('8', '100')
graph.add_edge('0', '96')
graph.add_edge('120', '156')
graph.add_edge('128', '160')


graph.add_edge('96', '100')
graph.add_edge('100', '160')
graph.add_edge('160', '156')
graph.add_edge('156', '96')

graph.add_edge('100', '146')
graph.add_edge('96', '144')
graph.add_edge('156', '174')
graph.add_edge('160', '176')

graph.add_edge('144', '146')
graph.add_edge('146', '176')
graph.add_edge('176', '174')
graph.add_edge('174', '144')

print(graph.vertices)

N = len(graph.vertices)
node_indices = list(graph.vertices)


plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1000), y_range=(-1.1,1000),
              tools='', toolbar_location=None)

graph_renderer = GraphRenderer()

graph_renderer.node_renderer.data_source.add(node_indices, 'index')
graph_renderer.node_renderer.data_source.add(['orange'], 'color')
graph_renderer.node_renderer.glyph = Circle(radius=0.4, fill_color='color')

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
x = [50 * (i // 15) for i in grid]
y = [50 * (i % 15) for i in grid]
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
