# #!/usr/bin/python

# """
# Demonstration of Graph and BokehGraph functionality.
# """
# import random
# from sys import argv
# from graph import Graph
# from draw import BokehGraph


# def main(v, e):
#     graph = Graph()
#     for i in range(v):
#         graph.add_vertex(i)
#     for j in range(e):
#         rand_vert = int(random.random() * v)
#         rand_edge = int(random.random() * e)
#         print(rand_vert, rand_edge)
#         graph.add_edge(rand_vert, rand_edge)
#     print(graph.vertices)
#     bokeh_graph = BokehGraph(graph)
#     bokeh_graph.show()


# if __name__ == '__main__':
#     if len(argv) > 1:
#         v = argv[1]
#         e = argv[2]
#     main(int(v), int(e))

import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

N = 8
node_indices = list(range(N))

plot = figure(title="Graph Layout Demonstration", x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
              tools="", toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(Spectral8, 'color')
graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color="color")

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

# start of layout code
circ = [i*2*math.pi/8 for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]
graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# Draw quadratic bezier paths


def bezier(start, end, control, steps):
    return [(1-s)**2*start + 2*(1-s)*s*control + s**2*end for s in steps]


xs, ys = [], []
sx, sy = graph_layout[0]
steps = [i/100. for i in range(100)]
for node_index in node_indices:
    ex, ey = graph_layout[node_index]
    xs.append(bezier(sx, ex, 0, steps))
    ys.append(bezier(sy, ey, 0, steps))
graph.edge_renderer.data_source.data['xs'] = xs
graph.edge_renderer.data_source.data['ys'] = ys

plot.renderers.append(graph)

output_file("graph.html")
show(plot)
