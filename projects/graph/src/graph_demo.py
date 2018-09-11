import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet
from bokeh.palettes import Spectral8

# Step 1: Instantiate your graph and make sure you're importing your graph correctly

from graph import Graph

graph = Graph()  
graph.add_vertex('1')
graph.add_vertex('11')
graph.add_edge('1', '11')
graph.add_vertex('6')
graph.add_vertex('3')
graph.add_edge('6', '3')
graph.add_vertex('8')
graph.add_vertex('5')
graph.add_edge('8', '5')
graph.add_vertex('2')
graph.add_vertex('9')
graph.add_edge('1', '2')
graph.add_edge('1', '5')
graph.add_edge('1', '3')
graph.add_edge('1', '9')
print(graph.vertices)

# Step 2: Set N = your graph

N = len(graph.vertices)

# Step 3: Change your graph into a list

node_indices = list(graph.vertices)

# Step 4: Decide on the layout of your graph: range, color, shape

plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1), y_range=(-1.1,10.1),
              tools='', toolbar_location=None)

graph_renderer = GraphRenderer()

graph_renderer.node_renderer.data_source.add(node_indices, 'index')

# Step 5: Make sure your number of colors adds up to your number of vertices (Spectral 8 will use random colors)

graph_renderer.node_renderer.data_source.add(['red', 'blue', 'green', 'orange', 'red', 'blue', 'green', 'orange' ], 'color')
graph_renderer.node_renderer.glyph = Circle(radius=0.35, fill_color='color')

# Step 6: Make connections: create empty array, go thru the vertices, go thru their edges, append new vertices, and new edges

start_indices = []
end_indices = []

for vertex in graph.vertices:
    for edge_end in graph.vertices[vertex]:
        start_indices.append(vertex)
        end_indices.append(edge_end)
print(start_indices)
print(end_indices)

# Step 7: Define the start end end of your graph

graph_renderer.edge_renderer.data_source.data = dict(
    start=start_indices,
    end=end_indices)

# Step 8: Layout the grid 

grid = [int(v) for v in graph.vertices]
x = [2 * (i // 3) for i in grid]
y = [2 * (i % 3) for i in grid]

# Use this code to make a circle graph
# circ = [int(i)*2*math.pi/8 for i in graph.vertices] (be sure to change `names=circle` in line 87)
# x = [math.cos(i) for i in circ]
# y = [math.sin(i) for i in circ]

# Use this code to make a parabolic graph (be sure to change `y_range=(-1.1,100.1)` line 40)
# grid = [int(v) for v in graph.vertices]
# x = [i for i in grid]
# y = [i ** 2 for i in grid]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph_renderer)

# Step 9: Add labels to nodes

labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
labels = LabelSet(x='x', y='y', text='names', level='glyph',
             text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

plot.add_layout(labels)

output_file('graph.html')
show(plot)