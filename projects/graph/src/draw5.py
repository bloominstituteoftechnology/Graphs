import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Circle, LabelSet
from bokeh.palettes import Spectral8

N = 8
node_indices = list(range(N))

# plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,5), y_range=(-1.1,5),
              tools='', toolbar_location=None, names=['Mark', 'Amir', 'Matt', 'Greg',
                                           'Owen', 'Juan'])

graph = GraphRenderer()


LabelSet(x='x', y='y', text='names', level='glyph',
         x_offset=5, y_offset=5, source=plot)

graph.node_renderer.data_source.add(node_indices, 'index')
# graph.node_renderer.data_source.add("Spectral8", 'color')
graph.node_renderer.data_source.add(["green"]*N, 'color')
graph.node_renderer.data_source.add_layout(labels)
# graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')
graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    # start=[0,0,1,4,0,4,7,0],
    end=node_indices)

### start of layout code
# circ = [i*2*math.pi/8 for i in node_indices]
# x = [math.cos(i) for i in circ]
# y = [math.sin(i) for i in circ]

x = [2*(i //3) for i in node_indices]
y = [2* (i % 3) for i in node_indices]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)