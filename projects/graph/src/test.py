import math
from graph import graph

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, LabelSet, ColumnDataSource
from bokeh.palettes import Spectral8

N = 8
node_indices = graph.get_vertices()

plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools='', toolbar_location=None)

grapher = GraphRenderer()

grapher.node_renderer.data_source.add(node_indices, 'index')
grapher.node_renderer.data_source.add(Spectral8, 'color')
grapher.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

grapher.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices
    )
print(grapher.edge_renderer.data_source.data)

### start of layout code
circ = [i*2*math.pi/8 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]

grapher_layout = dict(zip(node_indices, zip(x, y)))
grapher.layout_provider = StaticLayoutProvider(graph_layout=grapher_layout)

labels = LabelSet(
    x=x,
    y=y,
    text= 'index',
    level='glyph',
    x_offset=5, 
    y_offset=5, 
    source=ColumnDataSource('index'), 
    render_mode='canvas'
    )


plot.renderers.append(grapher)

output_file('graph.html')
plot.add_layout(labels)
show(plot)