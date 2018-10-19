"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Oval, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, Graph):
        self.Graph = Graph
    def draw(self):
        Graph = self.Graph

N = 8
node_indices = list(range(N))
print(node_indices)
plot = figure(title="Graph Layout Demonstration", x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools="", toolbar_location=None)
graph = GraphRenderer()
graph.node_renderer.data_source.add(node_indices, 'index')
node_colors = ['red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue']
graph.node_renderer.data_source.add(node_colors, 'color')
graph.node_renderer.glyph = Circle(radius=0.1, fill_color="color")
graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices
)
d = dict(
    start=[0]*N,
    end=node_indices
)      
print(d)

circ = [i*2*math.pi/8 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]
print(circ)
print(x)
print(y)
graph_layout = dict(zip(node_indices, zip(x, y)))

def bezier(start, end, control, steps):
    return [(1-s)**2*start + 2*(1-s)*s*control + s**2*end for s in steps]

xs, ys = [], []
sx, sy = graph_layout[0]
steps = [i/100 for i in range(100)]
for node_index in node_indices:
    ex, ey = graph_layout[node_index]
    xs.append(bezier(sx, ex, 0, steps))
    ys.append(bezier(sy, ey, 0, steps))
graph.edge_renderer.data_source.data['xs'] = xs
graph.edge_renderer.data_source.data['ys'] = ys

plot.renderers.append(graph)

output_file("graph.html")
show(plot)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')

bg = BokehGraph(Graph)
bg.draw()
