import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, DiamondCross
from bokeh.palettes import Viridis10
from bokeh.models.markers import DiamondCross

N = 10
node_indices = list(range(N))
# node_indices = [1, 2, 3, 4, 5, 6, 7, 8]

plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(Viridis10, 'color')
graph.node_renderer.glyph = DiamondCross(x="x", y="y", size="sizes", line_color="#386cb0", fill_color='color', line_width=2)

graph.edge_renderer.data_source.data = dict(
    start=(node_indices),
    end=([i + 4 for i in node_indices]))

### start of layout code
circ = [i*2*math.pi/10 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]

# x = [0,1,2,3,4,5,6,7]
# y = [0,1,2,3,4,5,6,7]
# print('circ',circ)
# print('x', x)
# print('y', y)

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)

